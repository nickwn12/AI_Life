import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
from parallelHillClimberCubes import PARALLEL_HILL_CLIMBER_CUBES
import random


random.seed(1)
phc = PARALLEL_HILL_CLIMBER_CUBES()
phc.Show_Body()
phc.EvolveAndSave()
# input("Press Enter to continue...")
# phc.Show_Best()
