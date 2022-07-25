# -*- coding: utf-8 -*-
"""
tail method .print last row of data set
"""

import pandas as pd
data=pd.read_csv('many_data.csv')
print(data.tail())
print(data.tail(10))