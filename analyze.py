import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg', linewidth="2")
matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg', linewidth="2")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
