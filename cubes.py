import random
import numpy as np
import pyrosim.pyrosim as pyrosim
from cube import CUBE
import constants as c


class CUBES:
    def __init__(self):
        self.cubes = {}
        self.familyTree = {}
        self.curIndx = 0

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

    def buildBody(self):
        pyrosim.Start_URDF("summerbod.urdf")

        torsoCube = self.cubes[0]
        # torsoCube = CUBE()

        if 0 in c.Sensors:
            colorName = "Blue"
            rgb = [1, 0, 1]
        else:
            colorName = "Green"
            rgb = [1, 1, 1]

        BaseHeight = self.returnMinZ()

        pyrosim.Send_Cube(name=str(torsoCube.cubeName), pos=[0, 0, -BaseHeight], size=[
            torsoCube.length, torsoCube.width, torsoCube.height], rgb=rgb)

        stack = list(self.familyTree[0])
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
            elif abs(Ydif) > abs(Zdif):
                yAnchorChild = .5
                if Ydif < 0:
                    yAnchorChild *= -1
            else:
                zAnchorChild = .5
                if Zdif < 0:
                    zAnchorChild *= -1

            if child.cubeName in c.Sensors:
                colorName = "Blue"
                rgb = [1, 0, 1]
            else:
                colorName = "Green"
                rgb = [1, 1, 1]

            pyrosim.Send_Joint(name="Joint" + str(parent.cubeName)+"_" + str(child.cubeName), parent=str(parent.cubeName),
                               child=str(child.cubeName), type="revolute", position=[parent.length * (xAnchor + xAnchorChild), parent.width * (yAnchor + yAnchorChild), parent.height * (zAnchor + zAnchorChild)], jointAxis="0 0 1"
                               )

            pyrosim.Send_Cube(name=str(child.cubeName), pos=[child.length * xAnchorChild, child.width * yAnchorChild, child.height * zAnchorChild - BaseHeight], size=[
                child.length, child.width, child.height], colorName=colorName, rgb=rgb)

            if child.cubeName in self.familyTree:
                stack += self.familyTree[child.cubeName]
            stack.pop(0)
        pyrosim.End()

        return

    def generateBrain(self):
        pyrosim.Start_NeuralNetwork("fuckthehaters.nndf")
        for i, sensorNum in enumerate(c.Sensors):
            pyrosim.Send_Sensor_Neuron(
                name=i, linkName=str(sensorNum))

        stack = self.familyTree[0]
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

        weights = np.random.rand(
            c.numSensors, c.numMotorNeurons) * 2 - 1

        for currentRow, sensorNum in enumerate(c.Sensors):
            for currentColumn in range(c.numLinks - 1):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensors, weight=weights[currentRow][currentColumn])

        pyrosim.End()
