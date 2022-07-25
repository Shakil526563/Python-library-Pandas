# -*- coding: utf-8 -*-
"""
assing a something in empty row
"""
import pandas as pd
df=pd.read_csv('dirtydata.csv')
df.dropna(inplace = True)

print(df.to_string())


