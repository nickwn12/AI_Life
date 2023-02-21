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
robotId = p.loadURDF("summerbod.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

for i in range(10000):
    p.stepSimulation()
    time.sleep(.01)
    print(i)
