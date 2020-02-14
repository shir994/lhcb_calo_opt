import sys
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import numpy as np


def read_param(file_path, param_name, separator="|"):
    with open(file_path) as _file:
        for line in _file:
            if param_name in line:
                split_vals = line.strip().split(separator)[1:-1]
                return np.array([float(value) for value in split_vals])
                

def replace(file_path, param_name, values, boundaries=None, separator="|", is_int=False, assign_equal=True):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if param_name in line:
                    line = param_name
                    line += " = " if assign_equal else " "
                    line += separator
                    for index, value in enumerate(values):
                        value = max(boundaries[index], value) if boundaries is not None else value
                        line += "{:d}".format(value) if is_int else "{0:.5f} ".format(value)
                        line += separator
                    line += "\n"
                new_file.write(line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


if __name__ == "__main__":
    vals = np.random.randn(18)
    print(vals)
    param_name = "cell_crystal_pitch_x"
    boundary_name = "cell_crystal_size_x"
    bounds = read_param("spacal-base_OnlyGAGG.cfg", boundary_name)
    replace("spacal-base_OnlyGAGG.cfg", param_name, vals, bounds)
    print(read_param("spacal-base_OnlyGAGG.cfg", param_name))

    replace("gps_electron.mac", "/run/beamOn", [120], separator='', is_int=True, assign_equal=False)
