import pandas as smie

df = smie.read_csv("data.csv")
df.tail(10)
# for x in df.index:
# print(df.loc[x, "Country"], df.loc[x, "Population"])
y=df.iloc[0:, 2]
x=df.iloc[0:, 0:2]
print(x)
print(y)

# print(df.loc[[1,3],["cn","pop"]])
# print(f"df["Country"] df["Popularion"]")dd