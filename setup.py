# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
from codecs import open
from os import path

setup(  
    name='epw', 
    version='0.0.0',  
    description='Lightweight Python package for editing EnergyPlus Weather (epw) files',  # Required
    url='https://github.com/building-energy/bredem2012',  # Optional
    author='Steven Firth',  # Optional
    author_email='s.k.firth@lboro.ac.uk',  # Optional
    packages=find_packages() # Required
    )
