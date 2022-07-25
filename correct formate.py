# -*- coding: utf-8 -*-
"""
Replace a correct formate to date column value using to_datetime() method
"""

import pandas as pd
data=pd.read_csv('dirtydata.csv')
data['Date']=pd.to_datetime(data['Date'])
print(data.to_string())