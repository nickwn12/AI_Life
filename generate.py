import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length, width, height = 1,1,1
x, y ,z = 0, 0, .5

for k in range(5):

    for j in range(5):
        z = .5
        length, width, height = 1, 1, 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
            z += 1
            length, width, height = length * .9, width * .9, height * .9
        y += 1 
    y = 0
    x += 1
pyrosim.End()
