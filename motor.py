import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    def Set_Value(self, robot, i):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot.robotId, jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL, targetPosition=self.motorValues[i], maxForce=50)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyaBackLeg
        self.offset = c.phaseOffsetBackLeg

        if self.jointName == "Torso_Back":
            self.frequency *= .5

        targetAngles = np.linspace(-np.pi, np.pi, c.numSteps)
        self.motorValues = np.sin(
            targetAngles * self.frequency + self.offset) * self.amplitude
