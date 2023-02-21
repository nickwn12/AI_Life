from cube import CUBE
from cubes import CUBES
import random
import time
import os
import constants as c


cubes = []
length, width, height = random.random() * c.scale + c.baseLength, c.baseWidth + random.random() * \
    c.scale, c.baseHeight + random.random() * c.scale
cube1 = CUBE(length, width, height, True, [0, 0, 0])
cubes = CUBES()
cubes.addCube(cube1)
cubes.addXCubes(c.numLinks)

os.system("rm summerbod.urdf")

time.sleep(.01)
cubes.buildBody()
cubes.generateBrain()
