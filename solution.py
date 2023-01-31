import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(3, 2) * 2 - 1

    def Start_Simulation(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        self.CreateWorld()
        os.system("python3 simulate.py " + directOrGUI +
                  " " + str(self.myID) + " &")

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
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[
            length, width, height])

        pyrosim.Send_Joint(name="Torso_Back", parent="Torso",
                           child="BackLeg", type="revolute", position=[1, 0, 1]
                           )

        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[
            length, width, height])

        pyrosim.Send_Joint(name="Torso_Front", parent="Torso",
                           child="FrontLeg", type="revolute", position=[2, 0, 1])

        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[
            length, width, height])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Back")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Front")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Back")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Front")

        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=2)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=2)

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + 3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
