import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.numSteps)

    def Get_Value(self, iter):
        if self.linkName == "sinWave":
            self.values[iter] = np.sin(iter/100)
        else:
            self.values[iter] = pyrosim.Get_Touch_Sensor_Value_For_Link(
                self.linkName)

    def Save_Values(self):
        np.save("data/" + self.linkName + ".npy", self.values)
