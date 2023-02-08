import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time


class ROBOT:
    def __init__(self, solutionID):

        self.motors = {}
        self.solutionID = solutionID

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        os.system("rm brain"+str(self.solutionID)+".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, itr):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(itr)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                # self.nn.Print()
                desiredAngle = self.nn.Get_Value_Of(
                    neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self, desiredAngle)
                # print(neuronName, jointName, desiredAngle, c.motorJointRange)

        #
        # for motor in self.motors:

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        yCoordinateOfLinkZero = positionOfLinkZero[1]
        f = open("temp"+str(self.solutionID)+".txt", "w")
        f.write(str(yCoordinateOfLinkZero))
        f.close()
        os.system("mv temp" + str(self.solutionID) +
                  ".txt fitness" + str(self.solutionID)+".txt")
