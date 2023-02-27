import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
from parallelHillClimberCubes import PARALLEL_HILL_CLIMBER_CUBES
phc = PARALLEL_HILL_CLIMBER_CUBES()
phc.Show_Body()
phc.Evolve()
phc.Show_Best()
input("Press Enter to continue...")
phc.Show_Best()

for i in range(5):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")
