__author__ = 'gururea'
import urllib
import sys

protein_id = str(sys.argv[1])

base_url = 'http://www.uniprot.org/uniprot/%s.txt'

protein_description = urllib.urlopen(base_url % protein_id).read()

for line in protein_description.split('\n'):
    line = line[5:]
    if line.startswith('GO'):
        bio_process = line.split(';')[2]
        if bio_process.startswith(' P:'):
            print bio_process[3:]
        if bio_process.startswith(' F:'):
            print bio_process[3:]

