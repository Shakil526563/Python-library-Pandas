# -*- coding: utf-8 -*-
"""
Remove wrong formate value
"""
import pandas as pd
data=pd.read_csv('dirtydata.csv')
data['Date']=pd.to_datetime(data["Date"])
data.dropna(subset=['Date'],inplace=True)
print(data.to_string())
