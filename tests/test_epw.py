# -*- coding: utf-8 -*-

import unittest
from epw import epw
from pprint import pprint
import pandas as pd

class TestEpw(unittest.TestCase):
    
# OBJECT CREATION
    
    def test_epw___init__(self):
        a=epw()
        self.assertIsInstance(a,epw)
        print(a)


    def test_epw_read(self):
        a=epw()
        a.read(r'C:\EnergyPlusV8-9-0\WeatherData\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw')
        print(a.headers)
        print(a.dataframe.columns)
        print(a.dataframe[['Year', 'Month', 'Day', 'Hour', 'Minute','Dry Bulb Temperature']].head())
        

    def test_modify(self):
        a=epw()
        a.read(r'C:\EnergyPlusV8-9-0\WeatherData\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw')
        
        a.headers['LOCATION'][0]='New_location'
        print(a.headers['LOCATION'])
        
        a.dataframe['Dry Bulb Temperature']=a.dataframe['Dry Bulb Temperature']+1.0
        print(a.dataframe[['Year', 'Month', 'Day', 'Hour', 'Minute','Dry Bulb Temperature']].head())
        
        a.write('new_epw_file.epw')

if __name__=='__main__':
    
    o=unittest.main(TestEpw())  
    