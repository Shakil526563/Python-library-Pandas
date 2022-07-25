# -*- coding: utf-8 -*-
"""
Finding Relationships between dataset
"""

import pandas as pd
data=pd.read_csv('dirtydata.csv')
data.corr()
print(data.corr())
