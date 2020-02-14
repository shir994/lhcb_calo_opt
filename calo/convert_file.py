import json
import numpy as np
import os
from parameter_imputer import read_param

output_data = np.load("./outputs/out.root_numpy.npy")

pitch_x = read_param("../spacal-simulation/spacal-base_OnlyGAGG.cfg", "cell_crystal_pitch_x")
pitch_y = read_param("../spacal-simulation/spacal-base_OnlyGAGG.cfg", "cell_crystal_pitch_y")

returned_params = {
    "params": pitch_x.tolist() + pitch_y.tolist(),
    "kinematics": output_data[:, 2:10].tolist(),
    "energy": output_data[:, 10:].tolist()
}

with open(os.path.join("./outputs/", "optimise_input.json"), "w") as f:
    json.dump(returned_params, f)