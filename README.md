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
>>> a=epw()
>>> a.read(r'C:\EnergyPlusV8-9-0\WeatherData\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw')
>>> print(a)

```

Viewing the header information:

```python
>>> d=a.headers # this is a dictionary of the header information
>>> print(d) 

```

Viewing the climate data
```python
>>> df=a.dataframe  # this is pandas dataframe
>>> print(df.head())

```

Modifying the header information:

```python
>>> 

```

Modifying the climate data:

```python
>>> 

```

Saving the modified .epw file:

```python
>>> a.save('new_epw_file.epw')
```



