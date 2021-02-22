#!/usr/bin/env python

"""
call 'pip install -e .' to install package locally for testing.
"""

from setuptools import setup

# build setup command
setup(
    name="records",
    version="0.0.1",
    author="Catherine Lan",
    author_email="yl4289@columbia.edu",
    description="A package to query gbif database",
    classifiers=["Programming Language :: Python :: 3"],
    )
