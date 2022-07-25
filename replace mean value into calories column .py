# -*- coding: utf-8 -*-
"""
replace mean value into calories column 
"""

import pandas as pd
data=pd.read_csv('dirtydata.csv')
a=data['Calories'].mean()
data['Calories'].fillna(a,inplace=True)
print(data.to_string())