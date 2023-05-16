import matplotlib as pl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from a_intro import year_list, wheat_price_list

# importing wanted object

year = np.array(year_list)
price = np.array(wheat_price_list)

plt.plot(year, price, 'o:r', ms = 6, mec = 'r', mfc = 'c')

# o:r - marker type-circle, marker size - 6, markerendgecolor-r, markerfacecolor-cyan
plt.show()