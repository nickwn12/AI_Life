import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.numSteps)
        print(self.values)

    def Get_Value(self, iter):
        self.values[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            self.linkName)
