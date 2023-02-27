from solution import SOLUTION
import constants as c
import copy
import os
from solutionCubes import SOLUTIONCUBES
import random


class PARALLEL_HILL_CLIMBER_CUBES:
    def __init__(self):
        os.system("rm brainCubes*.nndf")
        os.system("rm bodyCubes*.urdf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 1
        for i in range(c.populationSize):
            self.parents[i] = SOLUTIONCUBES(self.nextAvailableID)
            self.nextAvailableID += 1

        # self.parent = SOLUTION()

    def Evolve(self):
        self.Evaluate(self.parents)
        numberOfGenerations = c.numberOfGenerations
        for currentGeneration in range(numberOfGenerations):
            print("Cur Gen is", currentGeneration)
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()

    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")
            # solution.Wait_For_Simulation_To_End()
            # numberOfGenerations = c.numberOfGenerations
            # for currentGeneration in range(numberOfGenerations):
            #     self.Evolve_For_One_Generation()

        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()
        os.system("rm brainCubes*.nndf")
        os.system("rm bodyCubes*.urdf")

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        # print(self.children)

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        # fitnessDict = {}
        # worstScore = 1000000
        # for parent in self.parents:
        #     if self.parents[parent].fitness < self.children[parent].fitness:
        #         self.parents[parent] = copy.deepcopy(self.children[parent])
        #     fitnessDict[parent] = self.parents[parent].fitness
        #     if worstScore > self.parents[parent].fitness:
        #         worstScore = self.parents[parent].fitness

        # totalScore = 0
        # scoreDict = {}
        # for parent in self.parents:
        #     fitnessDict[parent] = fitnessDict[parent] - worstScore
        #     totalScore += fitnessDict[parent]
        # listParents = list(scoreDict.keys())
        # orderParents = listParents.sort(key=lambda par: scoreDict[par])

        # for i in range(len(listParents)//2):
        #     self.parents[orderParents[i]
        #                  ] = copy.deepcopy(self.parents[orderParents[-i]])

        best = 0
        for parent in self.parents:
            if self.parents[parent].fitness > self.parents[best].fitness:
                best = parent
        curBest = self.parents[best].fitness
        bestIsChild = False
        for parent in self.parents:
            if curBest < self.children[parent].fitness:
                curBest = self.children[parent].fitness
                bestIsChild = True
                bestChild = parent

        if bestIsChild:
            for parent in self.parents:
                if random.random() < .1:
                    self.parents[parent] = copy.deepcopy(
                        self.children[bestChild])
        else:
            if random.random() < .1:
                bstParent = copy.deepcopy(self.parents[best])
                for parent in self.parents:
                    self.parents[parent] = copy.deepcopy(bstParent)

    def Print(self):
        for parent in self.parents:
            print("\n", self.parents[parent].fitness,
                  self.children[parent].fitness)

    def Show_Best(self):
        bestindex = 0

        for parent in self.parents:
            print(self.parents[bestindex].fitness)
            self.parents[bestindex].fitness > self.parents[parent].fitness
            bestindex = parent
        self.parents[bestindex].Start_Simulation("GUI")

    def Show_Body(self):
        self.parents[0].Start_Simulation("GUI")
