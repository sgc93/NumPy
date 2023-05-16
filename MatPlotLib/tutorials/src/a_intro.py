import matplotlib as pl
from matplotlib import pyplot as plt
import pandas as pd

# start with displaying the version of the installed matplotlib
if __name__ == "__main__":
    print(f"The following works are done with Matplotlib library of version : {pl.__version__}")

mat_price_df = pd.read_csv("MatPlotLib\\tutorials\\resources\\rice_wheat_corn_prices.csv")
# print(mat_price_df)
# cleaning empty cells

# print(mat_price_df.isnull())
mat_price_df.dropna(inplace=True)
# print(mat_price_df.isnull())

# check for some wrong data and wrong data format

# if __name__ == "__main__":
#   print(mat_price_df.describe())
#   print(mat_price_df.info())   # no wrong data format

# # plotting with pandas
if __name__ == "__main__":
  mat_price_df.plot(kind = "bar", x= "Year", y= "Price_wheat_ton", color = "red", label = "wheat price")
  plt.title("30 year Price change of Wheat")
  plt.xlabel = "Year"
  plt.ylabel = "Price(USD)"
  plt.show()

# extracting sample data from DataFrame - mat_price_df

year_list = [1992]
wheat_price_list = [170.45]

for index in mat_price_df.index:
    year = 1992
    i = 0
    if (mat_price_df.loc[index, "Year"] > year):
        if(mat_price_df.loc[index, "Year"] != year_list[i]):
            if (year <= 2003):
                year_list.append(mat_price_df.loc[index, "Year"])
                wheat_price_list.append(mat_price_df.loc[index, "Price_wheat_ton"])
                year += 1
                i += 1

# print(year_list)
# print(wheat_price_list)
if __name__ == "__main__":
    plt.plot(year_list, wheat_price_list)
    plt.show()