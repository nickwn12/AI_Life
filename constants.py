import numpy as np
import random
numSteps = 1000
amplitudeFrontLeg = np.pi/2
frequencyFrontLeg = 500
phaseOffsetFrontLeg = 0
amplitudeBackLeg = np.pi/2
frequencyaBackLeg = 20
phaseOffsetBackLeg = 2
numberOfGenerations = 10
populationSize = 20
numLinks = 5
numSensors = random.randint(1, numLinks)
# numSensors = numLinks
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
