import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(
            c.numSensorNeurons, c.numMotorNeurons) * 2 - 1

    def Start_Simulation(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        self.CreateWorld()
        os.system("python3 simulate.py " + directOrGUI +
                  " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness"+str(self.myID)+".txt")
        # print(self.fitness)

    def Evaluate(self, directOrGUI):
        pass

    def CreateWorld(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(
            name="Box", pos=[5,  5, 5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        length, width, height = 1, 1, 1
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, .5 * height], size=[
            length, width, height])

        pyrosim.Send_Joint(name="Torso_Back", parent="Torso",
                           child="BackLeg", type="revolute", position=[length * 0, width * -1, height/2], jointAxis="0 0 1"
                           )

        pyrosim.Send_Cube(name="BackLeg", pos=[0, 0, -.15], size=[
            .2, 1, .2])

        pyrosim.Send_Joint(name="Back_Back2", parent="BackLeg",
                           child="Back2", type="revolute", position=[0, -.5, .0], jointAxis="0 1 0"
                           )

        pyrosim.Send_Cube(name="Back2", pos=[0, -.5, -.15], size=[
            .2, 1, .2])
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Back")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Back2")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Back")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Back_Back2")

        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=2)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=2)

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
