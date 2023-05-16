# reading CSV files

import pandas as pd

print("HATE CRIMES CSV FILE \n\n\n\n\n")
df = pd.read_csv("C:\\Users\\hp pavilion\\Documents\\Python\\Machine learning\\Python_libraries\\Pandas\\resources\\Files\\data-master\\hate-crimes\\hate_crimes.csv")

print(df)   # this will print only the first 5 and the last 5 rows

print(pd.options.display.max_rows)  # 60 - means if the file to be read is 

# methods

print("\n\n The first 10 header rows: \n\n")
print(df.head(10))

print("\n\n The last 9 header rows: \n\n")
print(df.tail(9))

print("\n\n Concise information about the dataframe:  \n\n")
print(df.info())

print("\n\n Statistics on the DataFrame:  \n\n")
print(df.describe())
