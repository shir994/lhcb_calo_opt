import json
import numpy as np
import os

output_data = np.load("./outputs/out.root_numpy.npy")

returned_params = {
    "params": "dummy",
    "kinematics": output_data[:, 2:10].tolist(),
    "energy": output_data[:, 10:].tolist()
}

with open(os.path.join("./outputs/", "optimise_input.json"), "w") as f:
    json.dump(returned_params, f)