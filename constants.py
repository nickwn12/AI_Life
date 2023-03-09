import numpy as np
import random
numSteps = 1000
amplitudeFrontLeg = np.pi/2
frequencyFrontLeg = 500
phaseOffsetFrontLeg = 0
amplitudeBackLeg = np.pi/2
frequencyaBackLeg = 20
phaseOffsetBackLeg = 2
numberOfGenerations = 300
populationSize = 10
numLinks = 10
# numSensors = random.randint(2 * numLinks//3, numLinks)
numSensors = numLinks
numSensors = 1
# Sensors = list(range(numLinks))
Sensors = random.sample(range(0, numLinks), k=numSensors)
Sensors.sort()
print(Sensors, numSensors)
numMotorNeurons = numLinks - 1
motorJointRange = 1
maxForce = 30
scale = .6
baseLength = .06
baseWidth = .06
baseHeight = .06
