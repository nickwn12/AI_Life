import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import matplotlib.pyplot

numSteps = 1000


amplitudeFrontLeg = np.pi/2
frequencyFrontLeg = 50
phaseOffsetFrontLeg = 0

amplitudeBackLeg = np.pi/2
frequencyaBackLeg = 50
phaseOffsetBackLeg = 2

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


targetAngles = np.linspace(-np.pi, np.pi, numSteps)
targetAnglesFrontLeg = np.sin(targetAngles * frequencyFrontLeg +
                              phaseOffsetFrontLeg) * amplitudeFrontLeg
targetAnglesBackLeg = np.sin(targetAngles * frequencyaBackLeg +
                             phaseOffsetBackLeg) * amplitudeBackLeg

# matplotlib.pyplot.plot(targetAngles)
# matplotlib.pyplot.show()
# exit()
p.setGravity(0, 0, -50)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(numSteps)
frontLegSensorValues = np.zeros(numSteps)

for i in range(numSteps):
    p.stepSimulation()
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_Back',
                                controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesBackLeg[i], maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_Front',
                                controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesFrontLeg[i], maxForce=50)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('Back')
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('Front')
    time.sleep(.01)

    print(i)

print(backLegSensorValues)
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()
