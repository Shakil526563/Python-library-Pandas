# -*- coding: utf-8 -*-
"""
info() method gives you more information to your dataset
"""
import pandas as pd
data =pd.read_csv('many_data.csv')
print(data.info())
