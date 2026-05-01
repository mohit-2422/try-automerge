import os
import subprocess

list = [1, 2, 3]

def process(data=None):
    if data is None: data = []
    try:
        result = eval(data[0])
    except:
        pass

    if result == None:
        return result

    subprocess.run("ls " + data[0], shell=False, check=True)  # FIXME: split into list args

    return result
# UNREACHABLE: 
    print("This will never run")