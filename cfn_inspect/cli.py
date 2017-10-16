# -*- coding: utf-8 -*-
import click
import crayons
import json
from cfn_flip import to_json
from .__version__ import __version__
import boto3
import sys
from botocore.exceptions import ValidationError, ClientError


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
                crayons.white("  {}\n    Exported as ".format(p), bold=True),
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
    try:
        cfc = boto3.client("cloudformation")
    except Exception as e:
        raise e
    try:
        res = cfc.validate_template(TemplateBody=t)
    except Exception as e:
        return (False, e.response['Error']['Message'])
    return (True, res)

def _greeter():
    return crayons.blue("cfn-inspect v{}, Dariusz Dwornikowski".format(__version__), bold=True)


@click.command()
@click.argument("template", type=click.File('r'))
@click.option("--version", is_flag=True, default=False, help="Show version and exit")
@click.option(
    "--verbose", "-v", is_flag=True, default=False, help="Be more verbose about the output")
@click.option("--validate", is_flag=True, default=False, help="Validate template with AWS")
def cli(template, verbose=False, validate=False, version=False):
    click.echo(_greeter(), err=True)
    if version:
        sys.exit(0)

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
        click.echo(
            "Could not determine the input format or format not sane: {}".format(e), err=True)
        sys.exit(1)

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
            click.echo(
                crayons.red("Can't validate the template AWS - template size exceeds 51200 bytes"),
                err=True)
            sys.exit(1)
        try:
            result = _boto_validate(template)
            if result[0] == True:
                print(crayons.cyan("Yay ! template is valid", bold=True))
            else:
                print(crayons.cyan(":(, template is not valid: {}".format(result[1]), bold=True))
        except Exception as e:
            click.echo(crayons.red("Problem with boto3 connection, {}".format(e)), err=True)
            sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    cli()
