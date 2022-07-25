# -*- coding: utf-8 -*-
"""
check out the maximum row in data file.i think first maximum values row will see

"""
import pandas as pd
data=pd.read_csv('many_data.csv')
max=pd.options.display.max_rows
print(max)
