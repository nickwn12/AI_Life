import random
import numpy as np
import pyrosim.pyrosim as pyrosim
from cube import CUBE
import constants as c
import copy


class CUBES:
    def __init__(self, x=c.numLinks):
        self.cubes = {}
        self.familyTree = {}
        self.curIndx = 0
        self.numSensors = c.numSensors
        self.Sensors = c.Sensors
        self.numMotorNeurons = c.numMotorNeurons
        self.weights = np.random.rand(
            self.numSensors, self.numMotorNeurons) * 2 - 1
        self.createBodyWithXCubes(x)

    def getWeights(self):
        return self.weights

    def setWeights(self, weights):
        self.weights = weights

    def mutate(self):
        if random.random() < .5:
            self.mutateBody()
        else:
            self.mutateBrain()

    def mutateBrain(self):
        randomRow = random.randint(0, self.numSensors - 1)
        randomColumn = random.randint(0, self.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def mutateBody(self):
        randomCube = self.getRandomCube()
        randomCube.mutateSize()

    def addCube1(self):
        length, width, height = random.random() * c.scale + c.baseLength, c.baseWidth + random.random() * \
            c.scale, c.baseHeight + random.random() * c.scale
        cube1 = CUBE(length, width, height, True, [0, 0, 0])
        self.addCube(cube1)
        return

    def createBodyWithXCubes(self, x=c.numLinks):
        self.addCube1()
        self.addXCubes(x)
        return

    def returnMinZ(self):
        MinZ = 0
        for cube in self.getCubesList():
            if cube.Zmin < MinZ:
                MinZ = cube.Zmin
        return MinZ

    def addCube(self, cube, parent=-1):
        cube.nameCube(self.curIndx, parent)

        self.cubes[self.curIndx] = cube
        if parent in self.familyTree:
            self.familyTree[parent].append(self.curIndx)
        else:
            self.familyTree[parent] = [self.curIndx]
        self.curIndx += 1

    def getCubesList(self):
        return list(self.cubes.values())

    def getRandomCube(self):
        return random.sample(list(self.cubes.values()), 1)[0]

    def mutateCubes(self):
        randomCube = self.getRandomCube()
        return randomCube.addCubeRandomSide(self)

    def addXCubes(self, x=c.numLinks):
        i = 0
        while i < x - 1:
            if self.mutateCubes():
                i += 1

    def createBody(self, fileName="summerbod.urdf"):
        pyrosim.Start_URDF(fileName)

        torsoCube = self.cubes[0]
        # torsoCube = CUBE()

        if 0 in c.Sensors:
            colorName = "Blue"
            rgb = [1, 0, 1]
        else:
            colorName = "Green"
            rgb = [1, 1, 1]

        BaseHeight = -self.returnMinZ()

        pyrosim.Send_Cube(name=str(torsoCube.cubeName), pos=[0, 0, 0], size=[
            torsoCube.length, torsoCube.width, torsoCube.height], rgb=rgb)

        stack = []
        for value in self.familyTree[0]:
            stack.append(value)
        # stack += self.familyTree[0]
        xAnchor = 0
        yAnchor = 0
        zAnchor = 0

        while len(stack) > 0:

            child = self.cubes[stack[0]]
            parent = self.cubes[child.parent]

            sign = -.5

            if parent.parent in self.familyTree and parent.cubeName != 0:
                grandparent = self.cubes[parent.parent]
                Xdif = parent.centerX - grandparent.centerX
                Ydif = parent.centerY - grandparent.centerY
                Zdif = parent.centerZ - grandparent.centerZ

                xAnchor = 0
                yAnchor = 0
                zAnchor = 0
                if abs(Xdif) > abs(Ydif) and abs(Xdif) > abs(Zdif):
                    xAnchor = .5
                    if Xdif < 0:
                        xAnchor *= -1
                elif abs(Ydif) > abs(Zdif):
                    yAnchor = .5
                    if Ydif < 0:
                        yAnchor *= -1
                else:
                    zAnchor = .5
                    if Zdif < 0:
                        zAnchor *= -1

            Xdif = child.centerX - parent.centerX
            Ydif = child.centerY - parent.centerY
            Zdif = child.centerZ - parent.centerZ
            xAnchorChild = 0
            yAnchorChild = 0
            zAnchorChild = 0

            if abs(Xdif) > abs(Ydif) and abs(Xdif) > abs(Zdif):
                xAnchorChild = .5
                if Xdif < 0:
                    xAnchorChild *= -1

                JointAxis1 = "1 0 0"
                JointAxis2 = "0 1 0"
            elif abs(Ydif) > abs(Zdif):
                yAnchorChild = .5
                if Ydif < 0:
                    yAnchorChild *= -1
                JointAxis1 = "0 1 0"
                JointAxis2 = "1 0 0"
            else:
                zAnchorChild = .5
                if Zdif < 0:
                    zAnchorChild *= -1
                JointAxis1 = "0 1 0"
                JointAxis2 = "1 0 0"

            if child.cubeName in self.Sensors:
                colorName = "Blue"
                rgb = [1, 0, 1]
            else:
                colorName = "Green"
                rgb = [1, 1, 1]

            pyrosim.Send_Joint(name="Joint" + str(parent.cubeName)+"_" + str(child.cubeName), parent=str(parent.cubeName),
                               child=str(child.cubeName), type="revolute", position=[parent.length * (xAnchor + xAnchorChild), parent.width * (yAnchor + yAnchorChild), parent.height * (zAnchor + zAnchorChild)], jointAxis=JointAxis1
                               )

            pyrosim.Send_Cube(name=str(child.cubeName), pos=[child.length * xAnchorChild, child.width * yAnchorChild, 0 + child.height * zAnchorChild], size=[
                child.length, child.width, child.height], colorName=colorName, rgb=rgb)

            if child.cubeName in self.familyTree:
                stack += self.familyTree[child.cubeName]
            stack.pop(0)
        pyrosim.End()

        return

    def createBrain(self, fileName="fuckthehaters.nndf"):
        pyrosim.Start_NeuralNetwork(fileName)
        for i, sensorNum in enumerate(c.Sensors):
            pyrosim.Send_Sensor_Neuron(
                name=i, linkName=str(sensorNum))
        stack = []
        stack += self.familyTree[0]
        # stack = self.familyTree[0]
        Name = 0
        while len(stack) > 0:
            child = self.cubes[stack[0]]
            parent = self.cubes[child.parent]
            pyrosim.Send_Motor_Neuron(
                name=Name + c.numSensors, jointName="Joint" + str(parent.cubeName)+"_" + str(child.cubeName))
            Name += 1
            if child.cubeName in self.familyTree:
                stack += self.familyTree[child.cubeName]
            stack.pop(0)

        for currentRow, sensorNum in enumerate(self.Sensors):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + self.numSensors, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
