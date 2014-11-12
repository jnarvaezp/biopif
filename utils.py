__author__ = 'Gururea'

import subprocess
import multiprocessing

def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def howmanycores():
    return multiprocessing.cpu_count()
