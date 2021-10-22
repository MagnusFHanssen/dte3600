import numpy as np
from mayavi import mlab


arr = np.genfromtxt("data/gradient_with_building.csv", delimiter=",")
arr = np.transpose(arr)


mlab.plot3d(arr[0], arr[1], arr[2], arr[3], tube_radius=4, line_width=0.3)

mlab.show()
