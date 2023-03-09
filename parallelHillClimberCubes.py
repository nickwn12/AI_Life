from solution import SOLUTION
import constants as c
import copy
import os
from solutionCubes import SOLUTIONCUBES
import random
import pickle
import numpy as np


class PARALLEL_HILL_CLIMBER_CUBES:
    def __init__(self):
        os.system("rm brainCubes*.nndf")
        os.system("rm bodyCubes*.urdf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 1
        self.generationsTrained = 0
        self.maxFit = None
        self.maxFitList = []
        self.graphData = np.zeros([c.numberOfGenerations, c.populationSize])
        for i in range(c.populationSize):
            self.parents[i] = SOLUTIONCUBES(self.nextAvailableID)
            self.nextAvailableID += 1

        # self.parent = SOLUTION()

    def save(self):

        dir_list = os.listdir("pickleFolder/")
        curMax = 0
        for fileName in dir_list:
            strNum = fileName.split("test")[-1]
            strNum = strNum.split(".")[0]
            Num = int(strNum)
            if Num > curMax:
                curMax = Num
        curMax += 1
        pickle.dump(self, open('pickleFolder/test'+str(curMax)+'.pkl', 'wb'))

    def saveGeneration(self, gen):
        pickle.dump(self, open(
            'generation/generation'+str(gen)+'.pkl', 'wb'))

    def Evolve(self):
        self.Evaluate(self.parents)
        numberOfGenerations = c.numberOfGenerations
        for currentGeneration in range(numberOfGenerations):
            print("Cur Gen is", currentGeneration)
            self.Evolve_For_One_Generation()

    def EvolveAndSave(self):
        self.Evaluate(self.parents)
        currentGeneration = 0
        while True:
            print("Cur Gen is", currentGeneration)
            self.Evolve_For_One_Generation()
            if currentGeneration % 10 == 0:
                self.saveGeneration(currentGeneration)
            currentGeneration += 1

    def recordGeneration(self):
        for parent in self.parents:
            curFit = self.parents[parent].fitness
            if self.maxFit is None or self.maxFit < curFit:
                self.maxFit = curFit
            self.graphData[self.generationsTrained][parent] = curFit

    def listRecordData(self):
        self.maxFitList = []
        for i in range(self.generationsTrained):
            curGenFit = max(self.graphData[i])
            self.maxFitList.append(curGenFit)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        # self.recordGeneration()

        self.Print()
        self.generationsTrained += 1

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

        for parent in self.parents:
            parentFit = self.parents[parent].fitness
            childFit = self.children[parent].fitness
            if parentFit < childFit:
                # This is to make sure that the robot was not flying or anything but I think it caused
                # Problems
                # if parentFit < childFit and abs(childFit/parentFit) < 10:
                self.parents[parent] = copy.deepcopy(self.children[parent])
        worstParent = 0
        worstScore = self.parents[worstParent].fitness

        bestParent = 0
        bestScore = self.parents[bestParent].fitness
        for parent in self.parents:
            if self.parents[parent].fitness > bestScore:
                bestScore = self.parents[parent].fitness
                bestParent = parent
            if self.parents[parent].fitness < worstScore:
                worstScore = self.parents[parent].fitness
                worstParent = parent
        # if random.random() * 3 < 2:
        if random.random() > 2:
            print(worstParent, bestParent)
            print(self.parents[worstParent].fitness)
            print(self.parents[bestParent].fitness)
            self.parents[worstParent] = copy.deepcopy(self.parents[bestParent])

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

        # best = 0
        # for parent in self.parents:
        #     if self.parents[parent].fitness > self.parents[best].fitness:
        #         best = parent

        # bstParent = copy.deepcopy(self.parents[best])
        # for parent in self.parents:
        #     if random.random() < .1:
        #         self.parents[parent] = copy.deepcopy(bstParent)

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
        print(self.parents[bestindex].fitness)
        self.parents[bestindex].Start_Simulation("GUI")

    def Show_All(self):
        bestindex = 0
        scores = []
        for parent in self.parents:
            scores.append((parent, self.parents[parent].fitness))
        scores.sort(key=lambda x: x[-1], reverse=True)
        for score in scores:
            if score[1] > 10:
                # continue
                nick = 5
            self.parents[score[0]].Start_Simulation("GUI")

    def Show_Body(self):
        self.parents[0].Start_Simulation("GUI")
