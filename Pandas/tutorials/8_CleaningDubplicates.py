# dialing with wrong formats

import pandas as pd

# example 1
df = pd.read_csv("resources\\dirtydata.csv")

print(df)   # notice row 11 and 12 - they are the same

# check for duplicates

print(df.duplicated())  # row 12 - True : means it is duplicate

# take action : drop the duplicate rows

cleaned_df = df.drop_duplicates()
print(cleaned_df)   # row 12 will be deleted