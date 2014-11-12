__author__ = 'gururea'
import click
import subprocess
from utils import cmd_exists
from Bio import SeqIO

'''
This is a main program and integrate all process, this process search information based in the structure of protein
'''


@click.command()
@click.option('--hmmalign', default=1, help='Number of greetings.')
@click.option('--parserhmmscan', default=1, help='Generate output Tabbed from output  hammer scan')
@click.option('--domain2graph', default=1, help='Generate graph for family of proteins')
def homology_uniprot(input_proteome):
    if cmd_exists("hmmsearch") == "True":
        for seq_record in SeqIO.parse(input_proteome, "fasta"):
            perfil_hmm = seq_record.id+".hmm"
            proteina_fasta = seq_record.id
            proteina_dbtl = seq_record.id+".dbtl"
            proteina_tblo = seq_record.id+".tblo"
            p = subprocess.Popen(['hmmsearch', "--cpu=3", '--domtblout', proteina_dbtl, '--tblout', proteina_tblo, perfil_hmm, 'uniprot_sprot.fasta'], stdout=subprocess.PIPE)
            output = p.communicate()[0]
            print  output

@click.option('--pfamhmmscan', default=1, help='Pfam Hmmer Scan')

@click.option('--getUniProt-SwissProt', default=1, help='Get Latest Version UniProt-SwissProt')
def uniprotswissprot ():
    if cmd_exists("wget") == "True":
        URL_PFam = "ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz"
        obternerUniprot = subprocess.Popen(['wget',"-P databases/",URL_PFam], stdout=subprocess.PIPE)
        output = obternerUniprot.communicate()[0]
        print output
    elif cmd_exists("gunzip") == "True":
        archivo_PFam = "uniprot_sprot.fasta.gz"
        extraer = subprocess.Popen(['gunzip',archivo_PFam,">","databases/"], stdout=subprocess.PIPE)
        output = extraer.communicate()[0]
        print  output
    else:
        print "Houston we have a problems!"

@click.option('--getPFamCurated', default=1, help='Pfam Hmmer Scan')
def getPFam ():
    if cmd_exists("wget") == "True":
        URL_PFam = "ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz"
        obternerPFam = subprocess.Popen(['wget',"-P databases/",URL_PFam], stdout=subprocess.PIPE)
        output = obternerPFam.communicate()[0]
        print output
    elif cmd_exists("gunzip") == "True":
        archivo_PFam = "Pfam-A.hmm.gz"
        extraer = subprocess.Popen(['gunzip',archivo_PFam,">","databases/"], stdout=subprocess.PIPE)
        output = extraer.communicate()[0]
        print  output
    print "Deberia estar listo"


@click.option('--getPFamNoCurated', default=1, help='Pfam Not curated Hmmer profiles for Scan')


@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    getPFam()
