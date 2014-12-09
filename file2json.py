import sys
import csv
from Bio import SeqIO

newfile = str(sys.argv[1])
json_file = open(newfile+".json","wb")
json_file.write('{\n\t"Protein":{')
def protein():
    for seq_record in SeqIO.parse(str(sys.argv[1]), "fasta"):
        json_file.write('\n\t\t"Name":"%s",' % seq_record.id)
        json_file.write('\n\t\t"Sequence":"%s"' % seq_record.seq)
        #print seq_record.id
        #print seq_record.seq
    json_file.write('\n\t},')

def homology():
    filename = str(sys.argv[1])
    json_file.write('\n\t"Homology":[')
    filex = filename + ".homology"
    with open(filex) as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        next(f)
        for line in reader:
            json_file.write('\n\t\t{')
            json_file.write('\n\t\t\t"ProteinName":"%s",' % line[0])
            json_file.write('\n\t\t\t"Length":"%s",' % line[1])
            json_file.write('\n\t\t\t"Target Name":"%s",' % line[2])
            json_file.write('\n\t\t\t"Begin":"%s",' % line[3])
            json_file.write('\n\t\t\t"End":"%s"' % line[4])
            json_file.write('\n\t\t},\n')
            #print line[0]
            #print line[1]
            #print line[2]
            #print line[3]
            #print line[4]
        json_file.write('\n\t],')

def domain():
    filename = str(sys.argv[1])
    filex = filename + ".out"
    json_file.write('\n\t"DomainProtein":[')
    with open(filex) as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        next(f)
        for line in reader:
            json_file.write('\n\t\t{')
            json_file.write('\n\t\t\t"QueryName":"%s",' % line[0])
            json_file.write('\n\t\t\t"Length":"%s",' % line[1])
            json_file.write('\n\t\t\t"Target Name":"%s",' % line[2])
            json_file.write('\n\t\t\t"Begin":"%s",' % line[3])
            json_file.write('\n\t\t\t"End":"%s"' % line[4])
            json_file.write('\n\t\t},\n')
            #print line[0]
            #print line[1]
            #print line[2]
            #print line[3]
            #print line[4]
        json_file.write('\n\t],')

def endjson():
    json_file.write('\n}')

protein()
homology()
domain()
endjson()


