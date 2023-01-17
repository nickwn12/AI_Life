import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
numSteps = 100

p.setGravity(0, 0, -50)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(numSteps)
frontLegSensorValues = np.zeros(numSteps)
for i in range(numSteps):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('Back')
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('Front')
    time.sleep(.01)
    print(i)

print(backLegSensorValues)
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()
