import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
from parallelHillClimberCubes import PARALLEL_HILL_CLIMBER_CUBES
import random

random.seed(1)
phc = PARALLEL_HILL_CLIMBER_CUBES()

solutionCube = phc.parents[0]
cubes = solutionCube.cubes
cubeDelete = cubes.cubes[2]
ChildrenList = cubes.getCubeChildren(cubeDelete)
# phc.Show_Body()
# cubes.turnOffSensor(2)
# cubes.turnOffChildrenSensors(cubeDelete)
# phc.Show_Body()
# cubes.turnOnSensor(5)

# for i in range(9):
#     cubes.turnOnSensor(i)
#     print(cubes.numSensors)
#     print(cubes.weights.shape)
#     print()
cubes.deleteCubeAndKids(cubeDelete)
phc.Show_Body()
cubes.mutateGrowCube()
phc.Show_Body()

nick = 5
