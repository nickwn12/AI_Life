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

        self.robotId = p.loadURDF("bodyCubes"+str(solutionID)+".urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_Robot()
        
        # self.nn = NEURAL_NETWORK("fuckthehaters.nndf")
        # os.system("rm brain"+str(self.solutionID)+".nndf")

    def Prepare_Robot(self):
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brainCubes"+str(self.solutionID)+".nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        self.sensors["sinWave"] = SENSOR("sinWave")

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
                desiredAngle = self.nn.Get_Value_Of(
                    neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self, desiredAngle)

    def Think(self, itr=0):
        self.nn.Update(itr=itr)

    def Get_FitnessHalfway(self):
        best = 10000000
        for i in range(c.numLinks):
            stateOfLinkZero = p.getLinkState(self.robotId, i)
            if stateOfLinkZero is None:
                continue
            positionOfLinkZero = stateOfLinkZero[0]
            yCoordinateOfLinkZero = positionOfLinkZero[1]
            if yCoordinateOfLinkZero < best:
                best = yCoordinateOfLinkZero

        f = open("tempHalfway"+str(self.solutionID)+".txt", "w")
        f.write(str(best))
        f.close()
        os.system("mv tempHalfway" + str(self.solutionID) +
                  ".txt fitnessHalfway" + str(self.solutionID)+".txt")

    def Get_Fitness(self):
        best = 10000000
        for i in range(c.numLinks):
            stateOfLinkZero = p.getLinkState(self.robotId, i)
            if stateOfLinkZero is None:
                continue
            positionOfLinkZero = stateOfLinkZero[0]
            yCoordinateOfLinkZero = positionOfLinkZero[1]
            if yCoordinateOfLinkZero < best:
                best = yCoordinateOfLinkZero

        f = open("fitnessHalfway"+str(self.solutionID)+".txt", "r")
        fitnessHalfway = float(f.read())
        f.close()
        os.system("rm fitnessHalfway"+str(self.solutionID)+".txt")

        f = open("temp"+str(self.solutionID)+".txt", "w")
        f.write(str(best - fitnessHalfway))
        f.close()
        os.system("mv temp" + str(self.solutionID) +
                  ".txt fitness" + str(self.solutionID)+".txt")
