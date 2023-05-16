# dialing with wrong formats

import pandas as pd


df = pd.read_csv("resources\\dirtydata.csv")

# check for wrong formats with value_counts()

# print(df["Date"].value_counts(sort=True, ascending=True))
# print(df["Calories"].value_counts(sort=True))
# print(df.info())
# print(df.describe())

print(df)  # notice that under Date column, row 22 and 26 have wrong format

# use to_datatime() method to convert to data format

df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset="Date", inplace=True)
print(df)

