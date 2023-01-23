from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c


class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -50)
        # pyrosim.Prepare_To_Simulate(robotId)

    def Run(self):
        for i in range(c.numSteps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            time.sleep(.01)

    # def __del__(self):
    #     p.disconnect()
