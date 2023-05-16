import matplotlib as pl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from a_intro import mat_price_df

# importing wanted object

year = np.array(mat_price_df["Year"])
price = np.array(mat_price_df["Price_wheat_ton"])

plt.plot(year, price)
plt.show()