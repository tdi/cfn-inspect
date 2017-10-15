![https://badge.fury.io/py/cfn-inspect](https://badge.fury.io/py/cfn-inspect.svg)
![https://pypi.python.org/pypi/cfn-inspect](https://img.shields.io/pypi/pyversions/cfn-inspect.svg)

# cfn-inspect: pretty print and inspect CloudFormation templates

Simple pretty printer for CloudFormation templates, in future it will also provide some validation and deep inspection in the future.

Supports both json and yaml templates. You can validate templates with `--validate` switch.

[![asciicast](https://asciinema.org/a/142549.png)](https://asciinema.org/a/142549)


# Installation

```$ pip install cfn-inspect```

# Usage 

```
$ Usage: cfn-inspect [OPTIONS] TEMPLATE

Options:
  --verbose / -v  Be more verbose about the output
  --validate      Validate template with AWS
  --help          Show this message and exit.  
```


# Author
Dariusz Dwornikowski, Nordcloud
