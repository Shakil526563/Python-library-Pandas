# -*- coding: utf-8 -*-
"""
if there is duplicate row exits ,then return true otherwise false
"""
import pandas as pd
data=pd.read_csv('dirtydata.csv')
print(data.duplicated())
