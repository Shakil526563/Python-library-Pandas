# -*- coding: utf-8 -*-
"""
To plot only the markers, you can use shortcut string 
notation parameter 'o', which means 'rings'.
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,10])
y=np.array([1,500])

plt.plot(x, y,'o')
"""use o """