from parameter_imputer import read_param, replace
import numpy as np
import sys

if __name__ == "__main__":
    param_name = "cell_crystal_pitch"
    boundary_name = "cell_crystal_size"
    params_size = 18

    n_events = int(sys.argv[2])
    params = np.array(list(map(float, sys.argv[1].strip().split(","))))
    # print(n_events)
    # print(params)
    # print(params.shape)

    for index, coord in enumerate(["_x", "_y"]):
        bounds = read_param("../spacal-simulation/spacal-base_OnlyGAGG.cfg", boundary_name + coord)
        replace("../spacal-simulation/spacal-base_OnlyGAGG.cfg", param_name + coord,
                params[index * params_size: (index + 1) * params_size], bounds)

        replace("../spacal-simulation/gps_electron.mac", "/run/beamOn",
                [n_events], separator='', is_int=True, assign_equal=False)