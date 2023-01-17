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


Create_Robot()
Create_World()
