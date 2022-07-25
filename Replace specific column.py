# -*- coding: utf-8 -*-
"""
replace a specific columm """
import pandas as pd
data=pd.read_csv('dirtydata.csv')
data['Date'].fillna("1/2/2022",inplace=True)
print(data.to_string())

