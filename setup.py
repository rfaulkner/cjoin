#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

__version__ = '0.1.1'

setup(
    name='cjoin',
    version=__version__,
    long_description=long_description,
    description='Conditional join module.',
    url='http://www.github.com/rfaulkner/cjoin',
    author="Ryan Faulkner",
    author_email="ryan.faulkner@mail.mcgil.ca",
    packages=['cjoin'],
classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    data_files=[('readme', ['README.md'])]
)
