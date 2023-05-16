# Correlation : clear relationship between columns of a DataFrame

import pandas as pd

metal_price_change = pd.read_csv("resources\\Metals_price_change\\metal_price_changes.csv")

metal_price_change.dropna(inplace=True)

  # print(metal_price_change)

  # correlation matric
if __name__ == "__main__":
  numeric_cols = metal_price_change.select_dtypes(include='number').columns
  corr_matrix = metal_price_change[numeric_cols].corr()
  print(corr_matrix)
  # conclusion based on the matrix
  # price of all metals are increased through time, rank of increasing price: silver > alum with good correlation, nickel > uran but with bad correlation
  # inflation rate of gold is highly increase with time
  # inflation rate of alumunium is slightly decrease as time increases, but bad correlation
  #  ...