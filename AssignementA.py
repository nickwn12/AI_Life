import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import matplotlib.pyplot
import constants as c
from simulation import SIMULATION
from robot import ROBOT
from world import WORLD
from generate import Generate_Brain

Generate_Brain()
simulation = SIMULATION()
simulation.Run()
# robot = ROBOT()
# world = WORLD()
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())


# targetAngles = np.linspace(-np.pi, np.pi, c.numSteps)
# targetAnglesFrontLeg = np.sin(targetAngles * c.frequencyFrontLeg +
#                               c.phaseOffsetFrontLeg) * c.amplitudeFrontLeg
# targetAnglesBackLeg = np.sin(targetAngles * c.frequencyaBackLeg +
#                              c.phaseOffsetBackLeg) * c.amplitudeBackLeg

# # matplotlib.pyplot.plot(targetAngles)
# # matplotlib.pyplot.show()
# # exit()
# p.setGravity(0, 0, -50)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = np.zeros(c.numSteps)
# frontLegSensorValues = np.zeros(c.numSteps)

# for i in range(c.numSteps):
#     p.stepSimulation()
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_Back',
#                                 controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesBackLeg[i], maxForce=50)
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_Front',
#                                 controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesFrontLeg[i], maxForce=50)
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('Back')
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('Front')
#     time.sleep(.01)

#     print(i)

# print(backLegSensorValues)
# np.save("data/backLegSensorValues.npy", backLegSensorValues)
# np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# p.disconnect()
