# epw
Lightweight Python package for editing EnergyPlus Weather (epw) files

**UNDER DEVELOPMENT**

## Overview

EnergyPlus weather files or .epw files are comma separated variable (csv) files which contain weather and location information. They are used to provide climate data for the energy simulations of the EnergyPlus simulation software.

This package provides a `epw` class for reading, modifying and saving .epw files.

## Usage

Reading a .epw file:

```python
>>> from epw import epw
>>> epw.read('C:\...)
>>> print(epw)

```







