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
        self.Joints = []
        self.numLinks = 0
        self.SensorsNeuronDic = {}
        self.numMotorNeurons = c.numMotorNeurons
        self.weights = np.random.rand(
            self.numSensors + 1, self.numMotorNeurons) * 2 - 1
        self.createBodyWithXCubes(x)

    def getWeights(self):
        return self.weights

    def setWeights(self, weights):
        self.weights = weights

    def mutateSensors(self):
        randomCube = self.getRandomCube()
        cubeName = randomCube.name
        if cubeName in self.Sensors:
            self.turnOffSensor(cubeName)
        else:
            self.turnOnSensor(cubeName)

    def mutateGrowCube(self):
        self.addXCubes(1)
        line = (np.random.rand(len(self.weights), 1) - .5) * 2
        self.weights = np.concatenate((self.weights, line), axis=1)
        cubeList = list(self.cubes.keys())
        cubeList.sort(reverse=True)
        largestCube = cubeList[0]
        # self.numLinks += 1
        self.turnOnSensor(largestCube)

    def mutate(self):
        randNum = random.random()
        if randNum < .3:
            randBody = random.random()
            if randBody < .5/10:
                self.mutateGrowCube()
            elif randBody < 1/10:
                self.deleteRandomCube()
            else:
                self.mutateBody()
        elif randNum < .9:
            self.mutateBrain()
        else:
            self.mutateSensors()

    def mutateBrain(self):
        randomRow = random.randint(0, self.numSensors)
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
        self.addXCubes(x - 1)
        return

    def deleteRandomCube(self):
        if self.numLinks == 1:
            return False
        needValidCube = True
        while needValidCube:
            randomCube = self.getRandomCube()
            if randomCube.parent != -1:
                needValidCube = False
        self.deleteCubeAndKids(randomCube)

    def getCubeChildren(self, cube):
        stack = [cube.name]
        children = []
        while len(stack) > 0:
            curCubeName = stack[0]
            if curCubeName in self.familyTree:
                for child in self.familyTree[curCubeName]:
                    stack.append(child)
                    children.append(child)
            stack.pop(0)
        return children

    def turnOffChildrenSensors(self, cube):
        childrenList = self.getCubeChildren(cube)
        for child in childrenList:
            self.turnOffSensor(child)
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
        self.numLinks += 1

    def turnOffSensor(self, name):
        if not name in self.Sensors:
            return True
        if len(self.Sensors) == 1:
            return False
        index = self.Sensors.index(name)
        self.weights = np.delete(self.weights, (index), axis=0)
        self.Sensors.remove(name)
        self.numSensors -= 1
        return True

    def deleteCubeAndKids(self, cube):
        self.turnOffChildrenSensors(cube)
        children = self.getCubeChildren(cube)
        childrenReversed = list(reversed(children))
        for child in childrenReversed:
            self.deleteCube(self.cubes[child])

    def removeNameFamilyTree(self, name):
        if name in self.familyTree:
            return False
        for parent in self.familyTree:
            if name in self.familyTree[parent]:
                self.familyTree[parent].remove(name)
                if len(self.familyTree[parent]) == 0:
                    self.familyTree.pop(parent)
                return True
        raise ValueError('You Tried to delete a cube not in the Family Tree')
        return True

    def deleteCube(self, cube):
        if cube.name in self.familyTree:
            raise ValueError('Deleted a Cube with Kids')
        if cube.name in self.Sensors:
            raise ValueError('Deleted a Cube with Sensor')

        self.removeNameFamilyTree(cube.name)
        index = self.Joints.index((cube.parent, cube.name))
        self.Joints.remove((cube.parent, cube.name))
        self.numMotorNeurons -= 1
        self.numLinks -= 1
        self.cubes.pop(cube.name)
        self.weights = np.delete(self.weights, (index), axis=1)

    def turnOnSensor(self, name):
        if name in self.Sensors:
            return

        line = (np.random.rand((self.numLinks - 1)) - .5) * 2
        self.weights = np.insert(self.weights, -1, line, axis=0)
        self.numSensors += 1
        self.Sensors.append(name)

        return

    def getCubesList(self):
        return list(self.cubes.values())

    def addJoint(self, parentName, childName):
        self.Joints.append((parentName, childName))

    def getRandomCube(self):
        return random.sample(list(self.cubes.values()), 1)[0]

    def mutateCubes(self):
        randomCube = self.getRandomCube()
        return randomCube.addCubeRandomSide(self)

    def addXCubes(self, x=c.numLinks):
        i = 0
        while i < x:
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

        pyrosim.Send_Cube(name=str(torsoCube.name), pos=[0, 0, 0], size=[
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

            if parent.parent in self.familyTree and parent.name != 0:
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

                JointAxis1 = "0 1 1"
                JointAxis2 = "0 1 0"
            elif abs(Ydif) > abs(Zdif):
                yAnchorChild = .5
                if Ydif < 0:
                    yAnchorChild *= -1
                JointAxis1 = "1 0 1"
                JointAxis2 = "1 0 0"
            else:
                zAnchorChild = .5
                if Zdif < 0:
                    zAnchorChild *= -1
                JointAxis1 = "1 1 0"
                JointAxis2 = "1 0 0"

            if child.name in self.Sensors:
                colorName = "Blue"
                rgb = [1, 0, 1]
            else:
                colorName = "Green"
                rgb = [1, 1, 1]

            pyrosim.Send_Joint(name="Joint" + str(parent.name)+"_" + str(child.name), parent=str(parent.name),
                               child=str(child.name), type="revolute", position=[parent.length * (xAnchor + xAnchorChild), parent.width * (yAnchor + yAnchorChild), parent.height * (zAnchor + zAnchorChild)], jointAxis=JointAxis1
                               )

            pyrosim.Send_Cube(name=str(child.name), pos=[child.length * xAnchorChild, child.width * yAnchorChild, 0 + child.height * zAnchorChild], size=[
                child.length, child.width, child.height], colorName=colorName, rgb=rgb)

            if child.name in self.familyTree:
                stack += self.familyTree[child.name]
            stack.pop(0)
        pyrosim.End()

        return

    def createBrain(self, fileName="fuckthehaters.nndf"):
        pyrosim.Start_NeuralNetwork(fileName)
        for i, sensorNum in enumerate(self.Sensors):
            pyrosim.Send_Sensor_Neuron(
                name=i, linkName=str(sensorNum))
        pyrosim.Send_Sensor_Neuron(
            name="sinWave", linkName=str("sinWave"))

        stack = []
        stack += self.familyTree[0]
        # stack = self.familyTree[0]
        Name = 0
        while len(stack) > 0:
            child = self.cubes[stack[0]]
            parent = self.cubes[child.parent]
            pyrosim.Send_Motor_Neuron(
                name=Name + self.numSensors, jointName="Joint" + str(parent.name)+"_" + str(child.name))
            Name += 1
            if child.name in self.familyTree:
                stack += self.familyTree[child.name]
            stack.pop(0)

        for currentRow, sensorNum in enumerate(self.Sensors):
            for currentColumn in range(self.numLinks - 1):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + self.numSensors, weight=self.weights[currentRow][currentColumn])
        for currentColumn in range(self.numLinks - 1):
            pyrosim.Send_Synapse(sourceNeuronName="sinWave",
                                 targetNeuronName=currentColumn + self.numSensors, weight=self.weights[-1][currentColumn])

        pyrosim.End()
