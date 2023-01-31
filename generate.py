import random
import pyrosim.pyrosim as pyrosim


length, width, height = 1, 1, 1
x, y, z = 0, 0, .5


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box", pos=[x - 5, y + 5, z], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[
                      length, width, height])

    pyrosim.Send_Joint(name="Torso_Back", parent="Torso",
                       child="BackLeg", type="revolute", position=[1, 0, 1]
                       )

    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[
        length, width, height])

    pyrosim.Send_Joint(name="Torso_Front", parent="Torso",
                       child="FrontLeg", type="revolute", position=[2, 0, 1])

    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[
        length, width, height])

    pyrosim.End()


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[
        length, width, height])

    pyrosim.Send_Joint(name="Torso_Back", parent="Torso",
                       child="BackLeg", type="revolute", position=[1, 0, 1]
                       )

    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[
        length, width, height])

    pyrosim.Send_Joint(name="Torso_Front", parent="Torso",
                       child="FrontLeg", type="revolute", position=[2, 0, 1])

    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[
        length, width, height])

    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="Back")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="Front")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Back")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Front")

    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=2)
    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=2)

    for i in range(3):
        for j in range(2):
            pyrosim.Send_Synapse(sourceNeuronName=i,
                                 targetNeuronName=i + 3, weight=(random.random() - .5) * 2)

    pyrosim.End()


# Create_Robot()
