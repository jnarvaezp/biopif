__author__ = 'Gururea'

import re
import sys


filename = (sys.argv[1])
new_file = filename.replace(".tab","")
text_file = open(new_file+".out", "wb")
print new_file

print 'protname\tlen\tdomname\tbegin\tend'
text_file.write('protname\tlen\tdomname\tbegin\tend\n')

for line in open(filename):
    if not re.search('^\#', line):  # avoid all lines beginning
                                    # with the '#' character

        col = re.split(' +', line)

        domname =  col[0]
        protname = col[2]

        protname = re.sub('.*\|', '', protname)
        length   = col[5]
        evalue   = float(col[12])
        begin    = col[17]
        end      = col[18]
        if evalue < 1e-5:
            text_file.write("%s\t" % protname)
            text_file.write("%s\t" % length)
            text_file.write("%s\t" % domname)
            text_file.write("%s\t" % begin)
            text_file.write("%s\n" % end)
            print protname, '\t', length, '\t', domname,
            print '\t', begin, '\t', end


#    text_file = open (seq_record.id, "wb")
 #   text_file.write(">%s" % seq_record.id )
 #   text_file.write("\n%s" % seq_record.seq)
 #   text_file.close()
 #   perfil_hmm = seq_record.id+".tab"
 #   proteina_fasta = seq_record.id
 #   p = subprocess.Popen(['hmmscan',"--cpu=2","--domtblout",perfil_hmm,"Pfam-B.hmm",proteina_fasta], stdout=subprocess.PIPE)
 #   output = p.communicate()[0]
 #   print  output
