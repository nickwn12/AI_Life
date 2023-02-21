from cube import CUBE
from cubes import CUBES
import random
cubes = []
cube1 = CUBE(1, 1, 1, True, [0, 0, 0])
cubes = CUBES()
cubes.addCube(cube1)

for i in range(10):
    cubes.mutateCubes()

cubes.buildBody()