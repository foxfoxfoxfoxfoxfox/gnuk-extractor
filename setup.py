#!/usr/bin/env python3

from setuptools import setup

from setuptools.command.install import install
from pip._internal import main as pip

setup(
    name='gnukextract',
    version='1.0.0',
    description='Extract PGP private key from Gnuk / Nitrokey Start firmware',
    packages=['gnukextract'],
    # TODO: replace once PGPy pull requests are merged and new version is published on PyPI
    install_requires=['PGPy'],
    entry_points={
        'console_scripts': [
            'gnuk-extractor = gnuk_extractor:main_func',
        ],
    }
)
