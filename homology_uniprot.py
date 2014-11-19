__author__ = 'Gururea'

import subprocess
from Bio import SeqIO

for seq_record in SeqIO.parse("tuberculosis.fa", "fasta"):
#    print(seq_record.id)
#    print(seq_record.seq)
#    text_file = open (seq_record.id, "wb")
#    text_file.write(">%s" % seq_record.id )
#    text_file.write("\n%s" % seq_record.seq)
#    text_file.close()
    perfil_hmm = seq_record.id+".hmm"
    proteina_fasta = seq_record.id
    proteina_dbtl = seq_record.id+".dbtl"
    proteina_tblo = seq_record.id+".tblo"
    p = subprocess.Popen(['hmmsearch',"--cpu=3",'--domtblout',proteina_dbtl,'--tblout',proteina_tblo,perfil_hmm,'uniprot_sprot.fasta'], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    print  output