# -*- coding: utf-8 -*-
"""
series with an index ,here user can assign a index number """
import pandas as pd
data=[1,2,3]
series=pd.Series(data,index=['x','y','z'])
print(series)
print(series['y'])