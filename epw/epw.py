# -*- coding: utf-8 -*-

import pandas as pd
import csv

class epw():
    """A class which represents an EnergyPlus weather (epw) file
    """
    
    def __init__(self):
        """
        """
        self.headers={}
        self.dataframe=pd.DataFrame()
            
    
    def read(self,fp):
        """Reads an epw file 
        
        Arguments:
            - fp (str): the file path of the epw file   
        
        """
        
        self.headers=self._read_headers(fp)
        self.dataframe=self._read_data(fp)
                
        
    def _read_headers(self,fp):
        """Reads the headers of an epw file
        
        Arguments:
            - fp (str): the file path of the epw file   
            
        Return value:
            - d (dict): a dictionary containing the header rows 
            
        """
        
        d={}
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                if row[0].isdigit():
                    break
                else:
                    d[row[0]]=row[1:]
        return d
    
    
    def _read_data(self,fp):
        """Reads the climate data of an epw file
        
        Arguments:
            - fp (str): the file path of the epw file   
            
        Return value:
            - df (pd.DataFrame): a DataFrame comtaining the climate data
            
        """
        
        names=['Year',
               'Month',
               'Day',
               'Hour',
               'Minute',
               'Data Source and Uncertainty Flags',
               'Dry Bulb Temperature',
               'Dew Point Temperature',
               'Relative Humidity',
               'Atmospheric Station Pressure',
               'Extraterrestrial Horizontal Radiation',
               'Extraterrestrial Direct Normal Radiation',
               'Horizontal Infrared Radiation Intensity',
               'Global Horizontal Radiation',
               'Direct Normal Radiation',
               'Diffuse Horizontal Radiation',
               'Global Horizontal Illuminance',
               'Direct Normal Illuminance',
               'Diffuse Horizontal Illuminance',
               'Zenith Luminance',
               'Wind Direction',
               'Wind Speed',
               'Total Sky Cover',
               'Opaque Sky Cover (used if Horizontal IR Intensity missing)',
               'Visibility',
               'Ceiling Height',
               'Present Weather Observation',
               'Present Weather Codes',
               'Precipitable Water',
               'Aerosol Optical Depth',
               'Snow Depth',
               'Days Since Last Snowfall',
               'Albedo',
               'Liquid Precipitation Depth',
               'Liquid Precipitation Quantity']
        
        first_row=self._first_row_with_climate_data(fp)
        df=pd.read_csv(fp,
                       skiprows=first_row,
                       header=None,
                       names=names)
        return df
        
        
    def _first_row_with_climate_data(self,fp):
        """Finds the first row with the climate data of an epw file
        
        Arguments:
            - fp (str): the file path of the epw file   
            
        Return value:
            - i (int): the row number
            
        """
        
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i,row in enumerate(csvreader):
                if row[0].isdigit():
                    break
        return i
        
        
    def write(self,fp):
        """Writes an epw file 
        
        Arguments:
            - fp (str): the file path of the new epw file   
        
        """
        
        with open(fp, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for k,v in self.headers.items():
                csvwriter.writerow([k]+v)
            for row in self.dataframe.itertuples(index= False):
                csvwriter.writerow(i for i in row)