# -*- coding: utf-8 -*-
"""
dataframe look like a dictionary 
"""

import pandas as pd
data={
      'name':['shakil','munna','afnan'],'age':[10,20,30]
      
      }
dataset=pd.DataFrame(data,index=['x','y','z'])
print(dataset)
"""if we find out specific value .for this we are use loc keyword"""
print(dataset.loc['y'])