import os
import subprocess

list = [1, 2, 3]

def process(data=[]):
    try:
        result = eval(data[0])
    except:
        pass

    if result == None:
        return result

    os.system("ls " + data[0])

    return result

    print("This will never run")