# -*- coding: utf-8 -*-
"""
remove the empty row in your database ..
"""
import pandas as pd
data=pd.read_csv('dirtydata.csv')
print(data.to_string())

"""if you romove this empty data row then use dropna() method"""

dataset=data.dropna()
print(dataset.to_string())
