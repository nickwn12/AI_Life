from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
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
            solution.Start_Simulation("GUI")
            # solution.Wait_For_Simulation_To_End()
            # numberOfGenerations = c.numberOfGenerations
            # for currentGeneration in range(numberOfGenerations):
            #     self.Evolve_For_One_Generation()

        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()

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
        for parent in self.parents:
            if self.children[parent].fitness > self.parents[parent].fitness:
                self.parents[parent] = self.children[parent]
        # best = 0
        # for parent in self.parents:
        #     if self.parents[parent].fitness > self.parents[best].fitness:
        #         best = parent
        # curBest = self.parents[best].fitness
        # bestIsChild = False
        # for parent in self.parents:
        #     if curBest < self.children[parent].fitness:
        #         curBest = self.children[parent].fitness
        #         bestIsChild = True
        #         bestChild = parent

        # if bestIsChild:
        #     for parent in self.parents:
        #         self.parents[parent] = copy.deepcopy(self.children[bestChild])
        # else:
        #     bstParent = copy.deepcopy(self.parents[best])
        #     for parent in self.parents:
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
        self.parents[bestindex].Start_Simulation("GUI")

    def Show_Body(self):
        self.parents[0].Start_Simulation("GUI")
