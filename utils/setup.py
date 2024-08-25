import click
from doc_generator import generate_doc
from parser import parse_code

@click.command()
@click.argument('file_path')
@click.option('--output', default='documentation.md', help='Output file for documentation.')
def cli(file_path, output):
    functions = parse_code(file_path)
    generate_doc(functions, output)

if __name__ == '__main__':
    cli()
