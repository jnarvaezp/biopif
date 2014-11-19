__author__ = 'Gururea'

import subprocess
import multiprocessing
import biopif

def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def howmanycores():
    return multiprocessing.cpu_count()

def estimateusagecoresperjob():
    max_cores = multiprocessing.cpu_count()-1
    return max_cores

def splitfile(file):
    splitfasta = subprocess.Popen(['pyfasta', "split","-n", estimateusagecoresperjob(), file], stdout=subprocess.PIPE)
    output = splitfasta.communicate()[0]
    return 0

def splitjobs():
    biopif.homology_uniprot()
    return 0
