import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np 
import constants as c

class ROBOT:
    def __init__(self):
        
        self.motors = {}


        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    
    def Sense(self, itr):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(itr)
    
    def Act(self, i):
        for motor in self.motors:
            self.motors[motor].Set_Value(self, i)
                                                                  

