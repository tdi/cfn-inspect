# -*- coding: utf-8 -*-
import click
import crayons
import json
from cfn_flip import to_json
from .__version__ import __version__
import boto3
import sys


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
            print("{}{}".format(
                crayons.white("  {}\n    Exported as".format(p), bold=True),
                crayons.red("{}".format(crayons.red(output['Export']['Name'])))))
        else:
            print(crayons.white("  {}".format(p), bold=True))


def _pprint_parameters(t, verbose=False):
    print(crayons.blue("Parameters", bold=True))
    for p in t:
        if verbose:
            print("  {} ({})".format(p, t[p]['Type']))
        else:
            print("  {}".format(p))


def _boto_validate(t):
    cfc = boto3.client("cloudformation")
    return cfc.validate_template(TemplateBody=t)


def _greeter():
    return crayons.blue("cfn-inspect v{}".format(__version__), bold=True)


@click.command()
@click.argument("template", type=click.File('r'))
@click.option("--verbose/-v", is_flag=True, default=False, help="Be more verbose about the output")
@click.option("--validate", is_flag=True, default=False, help="Validate template with AWS")
def cli(template, verbose=False, validate=False):
    click.echo(_greeter(), err=True)

    print("{}: {}".format(
        crayons.white("Inspecting template", bold=True), crayons.blue(template.name)))
    template = template.read()
    try:
        t = json.loads(template)
    except Exception as e:
        pass
    try:
        json_template = to_json(template)
        t = json.loads(json_template)
    except Exception as e:
        raise Exception("Could not determine the input format: {}", e)

    if 'Description' in t:
        print("{}: {}".format(
            crayons.white("Description", bold=True),
            crayons.white("{}".format(t['Description']), bold=False)))

    if 'Parameters' in t:
        _pprint_parameters(t['Parameters'], verbose=verbose)
    if 'Resources' in t:
        _pprint_resources(t['Resources'], verbose=verbose)
    if 'Outputs' in t:
        _pprint_outputs(t['Outputs'], verbose=verbose)

    if validate:
        if len(template) > 51200:
            click.echo(crayons.red("Can't validate with AWS - template size exceeds 51200 bytes"))
            sys.exit(1)
        try:
            result = _boto_validate(template)
            if 'Description' in result:
                print(crayons.cyan("Yay ! template is valid", bold=True))
        except Exception as e:
            click.echo(crayons.red("AWS credentials not working, {}".format(e)), err=True)
            sys.exit(1)


if __name__ == "__main__":
    cli()
