import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import matplotlib.pyplot
import constants as c
from simulation import SIMULATION
from robot import ROBOT
from world import WORLD
from generate import Generate_Brain
import sys

# Generate_Brain()

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
