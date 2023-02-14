from solution import SOLUTION
import constants as c
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")

        numberOfGenerations = c.numberOfGenerations
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()
        # print(self.parent.weights)
        # print(self.child.weights)

        self.child.Evaluate("DIRECT")

        self.Select()

        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child

    def Print(self):
        print("\nParent Fitness: ", self.parent.fitness)
        print("Child Fitness: ", self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
