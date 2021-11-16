import numpy as np
from mayavi import mlab
from stl import mesh


def custom_load_model(filename):
    model = mesh.Mesh.from_file(filename)
    x = model.x.flatten()
    y = model.y.flatten()
    z = model.z.flatten()
    t = [(0. + i * 3., 1. + i * 3., 2. + i * 3.) for i
         in range(0, int(x.size/3))]
    return x, y, z, t


arr = np.genfromtxt("data/gradient_with_building.csv", delimiter=",")
arr = np.transpose(arr)

mlab.plot3d(arr[0], arr[1], arr[2], arr[3], tube_radius=4, line_width=0.3)

terreng = custom_load_model('models/terreng.stl')

stor_terreng = custom_load_model('models/terreng_stort.stl')

bygg_1 = custom_load_model('models/hovedbygg.stl')

bygg_2 = custom_load_model('models/nabobygg.stl')

mlab.triangular_mesh(bygg_1[0], bygg_1[1], bygg_1[2], bygg_1[3], color=(0.9, 0.4, 0.3), name='New building')

mlab.triangular_mesh(bygg_2[0], bygg_2[1], bygg_2[2], bygg_2[3], color=(0.5, 0.5, 0.5), name='Old buildings')

surf1 = mlab.triangular_mesh(terreng[0], terreng[1], terreng[2], terreng[3], vmin=-73., vmax=73.,
                             name='Terrain fine detail', colormap='ocean')

surf1.module_manager.scalar_lut_manager.load_lut_from_file('misc/custom-ocean.lut')

surf2 = mlab.triangular_mesh(stor_terreng[0], stor_terreng[1], stor_terreng[2], stor_terreng[3], vmin=-73., vmax=74.,
                             name='Terrain large', colormap='ocean')

surf2.module_manager.scalar_lut_manager.load_lut_from_file('misc/custom-ocean.lut')

mlab.show()
