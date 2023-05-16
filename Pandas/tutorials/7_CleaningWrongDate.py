# dialing with wrong data values

import pandas as pd


df = pd.read_csv("resources\\dirtydata.csv")
df.dropna(inplace=True)
print(df)   
# notice that at row 7 under Duration column, the value is 450 and it seems like more wrong relatively
# assume that durations more that 100 are wrong data so they have to be cleaned

for x in df.index:
    if df.loc[x, 'Duration'] > 100:
        df.drop(x, inplace=True)
print(df)  # notice row 7, Duration - it will not exist