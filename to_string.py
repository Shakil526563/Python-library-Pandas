# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:36:41 2022

@author: WIN10
"""
import pandas as pd 
data= pd.read_csv('many_data.csv')
"""if print just dataset name .then compiler show first and last five column and row value"""
print(data)
"""if you use dataset with to_string condition .then compiler show all data value"""
print(data.to_string())
