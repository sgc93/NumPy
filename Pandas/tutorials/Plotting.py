# Ploting with pandas
import pandas as pd
import matplotlib.pyplot as plt
from Correlation import metal_price_change as mpc

mpc.plot(kind='scatter', x='Price_gold_infl', y='Year', color = 'darkblue', label='scatter')
plt.title('Gold Price Changes')

df = pd.read_csv("resources\\Files\\data-master\\births\\US_births_2000-2014_SSA.csv")
df.dropna(inplace=True)
df.plot(kind='hist', x='year', y='births', color = 'darkgreen')
plt.title('Births in America')

plt.show()