__author__ = 'Gururea'
import subprocess
from Bio import SeqIO

for seq_record in SeqIO.parse("tuberculosis.fa", "fasta"):
#    print(seq_record.id)
#    print(seq_record.seq)
    text_file = open (seq_record.id, "wb")
    text_file.write(">%s" % seq_record.id )
    text_file.write("\n%s" % seq_record.seq)
    text_file.close()
    perfil_hmm = seq_record.id+".tab"
    proteina_fasta = seq_record.id
    p = subprocess.Popen(['hmmscan',"--cpu=2","--domtblout",perfil_hmm,"Pfam-A.hmm",proteina_fasta], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    print  output