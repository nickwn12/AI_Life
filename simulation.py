from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -50)
        # pyrosim.Prepare_To_Simulate(robotId)

    def Run(self):
        self.robot.Prepare_Robot()
        for i in range(c.numSteps):
            if 300 == i:
                self.Get_FitnessHalfway()
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think(i)
            self.robot.Act()
            if self.directOrGUI == "GUI":
                time.sleep(.01)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def Get_FitnessHalfway(self):
        self.robot.Get_FitnessHalfway()
