# -----------------------------------------------------------------------------
# Name: setup.py
# Description:
# Version: 05/09/2019
# Requirements:
# Author: Kemp94

# Useful references:
# -----------------------------------------------------------------------------

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name="VerbTest",
        version="1.0.0",
        description="",
        author="Kemp94",
        url="",
        packages=find_packages(),
        long_description=read('README.md')
)
