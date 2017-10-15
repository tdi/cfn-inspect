# -*- coding: utf-8 -*-
import click
import crayons
import json
from .__version__ import __version__


def _pprint_resources(t, verbose=False):
    print(crayons.blue("Resources", bold=True))
    for p in t:
        if verbose:
            print("  {} ({})".format(p, t[p]['Type']))
        else:
            print("  {}".format(p))


def __decode_output(output):
    return output

def _pprint_outputs(t, verbose=False):
    print(crayons.blue("Outputs", bold=True))
    for p in t:
        output = t[p]
        if 'Export' in output:
            a = list(output['Export']['Name'].keys())[0]
            print(crayons.white("  {}\n    Exported as".format(p), bold=True), crayons.red("{}".format(crayons.red(output['Export']['Name']))))
        else:
            print(crayons.white("  {}".format(p), bold=True))

def _pprint_parameters(t, verbose=False):
    print(crayons.blue("Parameters", bold=True))
    for p in t:
        if verbose:
            print("  {} ({})".format(p, t[p]['Type']))
        else:
            print("  {}".format(p))


def _greeter():
    click.echo(crayons.blue("cfn-inspect v{}".format(__version__), bold=True), err=True)

@click.command()
@click.argument("template", type=click.File('rb'))
@click.option("--verbose", is_flag=True, default=False, help="Be more verbose about the output")
def cli(template, verbose):
    _greeter()
    print(crayons.white("Inspecting template:", bold=True), crayons.blue(template.name))
    t = json.loads(template.read())
    print(crayons.white("Description:"), crayons.white("{}".format(t['Description']), bold=True))

    if 'Parameters' in t:
        _pprint_parameters(t['Parameters'], verbose=verbose)
    if 'Resources' in t:
        _pprint_resources(t['Resources'], verbose=verbose)
    if 'Outputs' in t:
        _pprint_outputs(t['Outputs'], verbose=verbose)


if __name__ == "__main__":
    cli()
