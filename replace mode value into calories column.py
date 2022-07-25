# -*- coding: utf-8 -*-
"""
replace mode value into calories column 

"""

import pandas as pd
data=pd.read_csv('dirtydata.csv')
a=data['Calories'].mode()[0]
data['Calories'].fillna(a,inplace=True)
print(data.to_string())