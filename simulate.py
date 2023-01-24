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

Generate_Brain()
simulation = SIMULATION()
simulation.Run()
