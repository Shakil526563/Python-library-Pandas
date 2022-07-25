# -*- coding: utf-8 -*-
"""
replace value specific position."""
import pandas as pd
data=pd.read_csv("dirtydata.csv")
data.loc[7,"Date"]="1"
print(data)

