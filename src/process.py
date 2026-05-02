import ast
import os
import subprocess

list = [1, 2, 3]

def process(data=None):
    if data is None: data = []
    try:
        result = ast.literal_eval(data[0])
    except Exception as e:
        pass

    if result is None:
        return result

    subprocess.run("ls " + data[0], shell=False, check=True)  # FIXME: split into list args

    return result
# UNREACHABLE: 
    # UNREACHABLE: print("This will never run")