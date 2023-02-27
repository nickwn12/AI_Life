import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
from cubes import CUBES


class SOLUTIONCUBES:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.cubes = CUBES()

    def Start_Simulation(self, directOrGUI):
        self.cubes.createBody("bodyCubes" + str(self.myID) + ".urdf")
        self.cubes.createBrain("brainCubes" + str(self.myID) + ".nndf")
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
        pyrosim.End()

    def Mutate(self):
        self.cubes.mutate()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
