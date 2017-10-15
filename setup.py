from setuptools import find_packages, setup, Command
import os

# Taked from pipenv source
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "cfn_inspect", "__version__.py")) as f:
    exec(f.read(), about)

__version__ = about['__version__']
required = ['crayons', 'click', 'cfn_flip', 'boto3']

setup(
    name='cfn-inspect',
    version=__version__,
    description='CloudFormation printer and inspector',
    long_description=open('README.md').read(),
    author='Dariusz Dwornikowski',
    author_email='dariusz.dwornikowski@nordcloud.com',
    url='https://github.com/tdi/cfn-inspect',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': ['cfn-inspect=cfn_inspect:cli'],
    },
    install_requires=required,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License', 'Programming Language :: Python',
        'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ], )
