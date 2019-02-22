# -*- coding: utf-8 -*-

import unittest
from epw import epw
from pprint import pprint

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
        print(a.dataframe.head())
        

if __name__=='__main__':
    
    o=unittest.main(TestEpw())  
    