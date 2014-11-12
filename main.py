__author__ = 'gururea'
import click
'''
este es un comentario
'''


@click.command()
@click.option('--hmmalign', default=1, help='Number of greetings.')

@click.option('--parserhmmscan', default=1, help='Generate output Tabbed from outputa hammer scan')

@click.option('--domain2graph', default=1, help='Generate graph for family of proteins')

@click.option('--hmmhomology', default=1, help='Finding Homology for proteome')

@click.option('--pfamhmmscan', default=1, help='Pfam Hmmer Scan')

@click.option('--getUniProt-SwissProt', default=1, help='Get Latest Version UniProt-SwissProt')

@click.option('--getPFam', default=1, help='Pfam Hmmer Scan')

@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()