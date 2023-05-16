# reading JSON file

import pandas as pd

# read the json file of the subtitle of Game of Thrones, season 4

season_4 = pd.read_json("C:\\Users\\hp pavilion\\Documents\\Python\\Machine learning\\Python_libraries\\Pandas\\resources\\GOT_subtitle\\season4.json")

# print the json file in DataFrame form

# topics of each episode of the season
# print(season_4.columns)

# sample dialogs in dataframe form - 5 rows from the start and 5 from the end
# print(season_4)

# full dialogs in dataframe form
# print(season_4.to_string())

# print some rows
print(season_4.head(10))
print(season_4.tail(12))