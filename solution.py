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
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[
            length, width, height])

        pyrosim.Send_Joint(name="Torso_Back", parent="Torso",
                           child="BackLeg", type="revolute", position=[0, -.5, 1], jointAxis="1 0 0"
                           )

        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[
            .2, 1, .2])

        pyrosim.Send_Joint(name="Torso_Left", parent="Torso",
                           child="LeftLeg", type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0"
                           )

        pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0, 0], size=[
            1, .2, .2])

        pyrosim.Send_Joint(name="Torso_Front", parent="Torso",
                           child="FrontLeg", type="revolute", position=[0, .5, 1], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[
            .2, 1, .2])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg",
                           child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -.5], size=[
            .2, .2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg",
                           child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5], size=[
            .2, .2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg",
                           child="LeftLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.5], size=[
            .2, .2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg",
                           child="RightLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5], size=[
            .2, .2, 1])

        pyrosim.Send_Joint(name="Torso_Right", parent="Torso",
                           child="RightLeg", type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0"
                           )

        pyrosim.Send_Cube(name="RightLeg", pos=[-0.5, 0, 0], size=[
            1, .2, .2])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Back")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Front")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="Left")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="Right")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_Back")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_Front")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_Left")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_Right")
        pyrosim.Send_Motor_Neuron(name=10, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="RightLeg_RightLowerLeg")

        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=2)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=2)

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
