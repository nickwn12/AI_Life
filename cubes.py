import random
import numpy as np
import pyrosim.pyrosim as pyrosim
from cube import CUBE


class CUBES:
    def __init__(self):
        self.cubes = {}
        self.familyTree = {}
        self.curIndx = 0

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
        randomCube.addCubeRandomSide(self)

    def buildBody(self):
        pyrosim.Start_URDF("summerbod.urdf")

        torsoCube = self.cubes[0]
        # torsoCube = CUBE()
        pyrosim.Send_Cube(name=str(torsoCube.cubeName), pos=[0, 0, 0], size=[
            torsoCube.length, torsoCube.width, torsoCube.height])

        stack = list(self.familyTree[0])
        while len(stack) > 0:
            child = self.cubes[stack[0]]
            parent = self.cubes[child.parent]
            Xdif = child.centerX - parent.centerX
            Ydif = child.centerY - parent.centerY
            Zdif = child.centerZ - parent.centerZ

            if abs(Xdif) > abs(Ydif) and abs(Xdif) > abs(Zdif):
                sign = 1
                if Xdif < 0:
                    sign = -1

                pyrosim.Send_Joint(name="Joint" + str(parent.cubeName)+"_" + str(child.cubeName), parent=str(parent.cubeName),
                                   child=str(child.cubeName), type="revolute", position=[sign * parent.length, 0, .0], jointAxis="0 0 1"
                                   )

                pyrosim.Send_Cube(name=str(child.cubeName), pos=[child.width * sign, 0, 0], size=[
                    child.length, child.width, child.height])
            elif abs(Ydif) > abs(Zdif):
                nick = 5
            else:
                nick = 5

            stack.pop(0)
        pyrosim.End()

        nick = 5
