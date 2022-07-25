# -*- coding: utf-8 -*-
"""
If we drop duplicate data 
"""
import pandas as pd
data=pd.read_csv('dirtydata.csv')
data.drop_duplicates(inplace=True)
print(data)

