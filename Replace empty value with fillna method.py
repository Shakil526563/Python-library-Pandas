# -*- coding: utf-8 -*-
"""
Replace empty value with fillna() method
"""
import pandas as pd
data=pd.read_csv('dirtydata.csv')
data.fillna(122,inplace=True)
print(data.to_string())
