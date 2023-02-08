import numpy as np

numSteps = 10000
amplitudeFrontLeg = np.pi/2
frequencyFrontLeg = 500
phaseOffsetFrontLeg = 0
amplitudeBackLeg = np.pi/2
frequencyaBackLeg = 20
phaseOffsetBackLeg = 2
numberOfGenerations = 10
populationSize = 10
numSensorNeurons = 10
numMotorNeurons = numSensorNeurons - 2
motorJointRange = 1
maxForce = 90
