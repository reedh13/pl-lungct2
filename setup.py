from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'lungct',
    version          = '1.0.0',
    description      = 'This plugin simply copies a specific lung image of interest to its output directory.',
    long_description = readme,
    author           = 'FNNDSC',
    author_email     = 'dev@babyMRI.org',
    url              = 'http://wiki',
    packages         = ['lungct', 'data'],
    install_requires = ['chrisapp~=2.0.0', 'pudb'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.8',
    entry_points     = {
        'console_scripts': [
            'lungct = lungct.__main__:main'
            ]
        }
)
