import pandas as pd

df = pd.read_csv("tutorials\\resources\\rice_wheat_corn_prices.csv")
# print(df)
df.dropna(inplace=True)
# print(df.isnull())

h = df.head(10)

x = h.iloc[0:,0:5]
y = h.iloc[0:,5:5:]
print(x, y)