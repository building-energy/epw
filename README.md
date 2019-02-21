# epw
Lightweight Python package for editing EnergyPlus Weather (epw) files

**UNDER DEVELOPMENT**

## Overview

EnergyPlus weather files or .epw files are comma separated variable (csv) files which contain weather and location information. They are used to provide climate data for the energy simulations of the EnergyPlus simulation software.

epw files can be difficult to work with because:
- the file is separated into 2 distinct sections, with the first 10 lines containing 'header' information and the remaining lines containing hourly weather values
- column headings are not provided in the file




