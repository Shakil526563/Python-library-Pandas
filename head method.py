# -*- coding: utf-8 -*-
"""
for quick overview ,here use the head method ..that means top value in dataset in print.
the number of row will specified head(10)..without specified head method print first five 
value in data set 
"""

import pandas as pd
data=pd.read_csv('many_data.csv')
print(data.head())
print(data.head(10))
"""first ten value will print"""