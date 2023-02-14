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
            c.numSensors, c.numMotorNeurons) * 2 - 1

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

        length, width, height = random.random() * c.scale + c.baseLength, c.baseWidth + random.random() * \
            c.scale, c.baseHeight + random.random() * c.scale

        pyrosim.Start_URDF("body.urdf")

        if 0 in c.Sensors:
            colorName = "Blue"
            rgb = [1, 0, 1]
        else:
            colorName = "Green"
            rgb = [1, 1, 1]

        pyrosim.Send_Cube(name="Back0", pos=[0, 0, 0], size=[
            length, width, height], colorName=colorName, rgb=rgb)
        width *= .5

        for i in range(c.numLinks - 1):

            if i % 3 == 1:
                curSize = [.1, 1, .1]
                jointAxis = "0 0 1"
            elif i % 3 == 2:
                curSize = [.4, 1, .2]
                jointAxis = "1 0 0"
            else:
                jointAxis = "0 0 1"
                curSize = [.2, 1, .4]

            pyrosim.Send_Joint(name="Back" + str(i)+"_Back" + str(i + 1), parent="Back" + str(i),
                               child="Back" + str(i + 1), type="revolute", position=[0, -width, .0], jointAxis=jointAxis
                               )

            length, width, height = random.random() * c.scale + c.baseLength, c.baseWidth + random.random() * \
                c.scale, c.baseHeight + random.random() * c.scale
            curSize = [length, width, height]

            if i in c.Sensors:
                colorName = "Blue"
                rgb = [1, 0, 1]
            else:
                colorName = "Green"
                rgb = [1, 1, 1]

            pyrosim.Send_Cube(name="Back" + str(i + 1),
                              pos=[0, -.5 * width, -.15], size=curSize, colorName=colorName, rgb=rgb)

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensors - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID)+".nndf")

        for i, sensorNum in enumerate(c.Sensors):
            pyrosim.Send_Sensor_Neuron(
                name=i, linkName="Back" + str(sensorNum))

        for i in range(c.numLinks - 1):
            pyrosim.Send_Motor_Neuron(
                name=i + c.numSensors, jointName="Back"+str(i)+"_Back"+str(1 + i))

        for currentRow, sensorNum in enumerate(c.Sensors):
            for currentColumn in range(c.numLinks - 1):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensors, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
