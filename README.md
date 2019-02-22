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
<epw.epw.epw object at 0x00000155BBAB99E8>
```

Viewing the header information:

```python
>>> d=a.headers # this is a dictionary of the header information
>>> print(d) 
{'LOCATION': ['San Francisco Intl Ap', 'CA', 'USA', 'TMY3', '724940', '37.62', '-122.40', '-8.0', '2.0'], 
 'DESIGN CONDITIONS': ['1', 'Climate Design Data 2009 ASHRAE Handbook', '', 'Heating', '1', '3.8', '4.9', '-3.7', '2.8', '10.7', '-1.2', '3.4', '11.2', '12.9', '12.1', '11.6', '12.2', '2.2', '150', 'Cooling', '8', '8.5', '28.3', '17.2', '25.7', '16.7', '23.6', '16.2', '18.6', '25.7', '17.8', '23.9', '17', '22.4', '5.9', '310', '16.1', '11.5', '19.9', '15.3', '10.9', '19.2', '14.7', '10.4', '18.7', '52.4', '25.8', '49.8', '23.8', '47.6', '22.4', '2038', 'Extremes', '12.8', '11.5', '10.6', '22.3', '1.8', '34.6', '1.5', '2.3', '0.8', '36.2', '-0.1', '37.5', '-0.9', '38.8', '-1.9', '40.5'],
 'TYPICAL/EXTREME PERIODS': ['6', 'Summer - Week Nearest Max Temperature For Period', 'Extreme', '8/ 1', '8/ 7', 'Summer - Week Nearest Average Temperature For Period', 'Typical', '9/ 5', '9/11', 'Winter - Week Nearest Min Temperature For Period', 'Extreme', '2/ 1', '2/ 7', 'Winter - Week Nearest Average Temperature For Period', 'Typical', '2/15', '2/21', 'Autumn - Week Nearest Average Temperature For Period', 'Typical', '12/ 6', '12/12', 'Spring - Week Nearest Average Temperature For Period', 'Typical', '5/29', '6/ 4'], 
 'GROUND TEMPERATURES': ['3', '.5', '', '', '', '10.86', '10.57', '11.08', '11.88', '13.97', '15.58', '16.67', '17.00', '16.44', '15.19', '13.51', '11.96', '2', '', '', '', '11.92', '11.41', '11.51', '11.93', '13.33', '14.60', '15.61', '16.15', '16.03', '15.32', '14.17', '12.95', '4', '', '', '', '12.79', '12.27', '12.15', '12.31', '13.10', '13.96', '14.74', '15.28', '15.41', '15.10', '14.42', '13.60'], 
 'HOLIDAYS/DAYLIGHT SAVINGS': ['No', '0', '0', '0'], 
 'COMMENTS 1': ['Custom/User Format -- WMO#724940; NREL TMY Data Set (2008); Period of Record 1973-2005 (Generally)'], 
 'COMMENTS 2': [' -- Ground temps produced with a standard soil diffusivity of 2.3225760E-03 {m**2/day}'], 
 'DATA PERIODS': ['1', '1', 'Data', 'Sunday', ' 1/ 1', '12/31']}
```

Viewing the climate data
```python
>>> df=a.dataframe  # this is pandas dataframe
>>> print(df.head())
   Year  Month  Day  Hour  Minute  \
0  1999      1    1     1       0   
1  1999      1    1     2       0   
2  1999      1    1     3       0   
3  1999      1    1     4       0   
4  1999      1    1     5       0   

                   Data Source and Uncertainty Flags  Dry Bulb Temperature  \
0  ?9?9?9?9E0?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9*9*9?9...                   7.2   
1  ?9?9?9?9E0?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9*9*9?9...                   7.2   
2  ?9?9?9?9E0?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9*9*9?9...                   6.7   
3  ?9?9?9?9E0?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9*9*9?9...                   6.1   
4  ?9?9?9?9E0?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9*9*9?9...                   4.4   

   Dew Point Temperature  Relative Humidity  Atmospheric Station Pressure  \
0                    5.6                 90                        102200   
1                    5.6                 90                        102100   
2                    5.0                 89                        102200   
3                    5.0                 93                        102200   
4                    3.9                 97                        102200   

   Extraterrestrial Horizontal Radiation  \
0                                      0   
1                                      0   
2                                      0   
3                                      0   
4                                      0   

   Extraterrestrial Direct Normal Radiation  \
0                                         0   
1                                         0   
2                                         0   
3                                         0   
4                                         0   

   Horizontal Infrared Radiation Intensity  Global Horizontal Radiation  \
0                                      290                            0   
1                                      296                            0   
2                                      291                            0   
3                                      276                            0   
4                                      280                            0   

   Direct Normal Radiation  Diffuse Horizontal Radiation  \
0                        0                             0   
1                        0                             0   
2                        0                             0   
3                        0                             0   
4                        0                             0   

   Global Horizontal Illuminance  Direct Normal Illuminance  \
0                              0                          0   
1                              0                          0   
2                              0                          0   
3                              0                          0   
4                              0                          0   

   Diffuse Horizontal Illuminance  Zenith Luminance  Wind Direction  \
0                               0                 0               0   
1                               0                 0             170   
2                               0                 0             210   
3                               0                 0             200   
4                               0                 0             260   

   Wind Speed  Total Sky Cover  \
0         0.0                2   
1         2.1                4   
2         2.1                3   
3         1.5                0   
4         3.1                3   

   Opaque Sky Cover (used if Horizontal IR Intensity missing)  Visibility  \
0                                                  2                 16.0   
1                                                  4                 16.0   
2                                                  3                 16.0   
3                                                  0                 16.0   
4                                                  3                 16.0   

   Ceiling Height  Present Weather Observation  Present Weather Codes  \
0           77777                            9              999999999   
1           77777                            9              999999999   
2           77777                            9              999999999   
3           77777                            9              999999999   
4           77777                            9              999999999   

   Precipitable Water  Aerosol Optical Depth  Snow Depth  \
0                 129                  0.108           0   
1                 120                  0.108           0   
2                 120                  0.108           0   
3                 120                  0.108           0   
4                 120                  0.108           0   

   Days Since Last Snowfall  Albedo  Liquid Precipitation Depth  \
0                        88    0.16                         0.0   
1                        88    0.16                         0.0   
2                        88    0.16                         0.0   
3                        88    0.16                         0.0   
4                        88    0.16                         0.0   

   Liquid Precipitation Quantity  
0                            1.0  
1                            1.0  
2                            1.0  
3                            1.0  
4                            1.0 
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



