# cleaning empty cells

import pandas as pd

df = pd.read_csv("C:\\Users\\hp pavilion\\Documents\\Python\\Machine learning\\Python_libraries\\Pandas\\resources\\Titanic_Uncleaned\\titanic_train.csv")

# sample view
# print(df.head(5))

# check for the precense of Empty Cells
print(df.isnull())  # sample empty cells :- col: Cabin- 0,2,4,...,886,888,890 ; col: age- 888

# method 1 - droping the rows that contain empty cells
cleaned_df = df.dropna()  # without affecting the original dataframe
# print(cleaned_df.isnull().to_string())  # all cells will have False value

# df.dropna(inplace=True)  # by affecting the original dataframe
# print(df.isnull())  # all cell must have False value

# method 2 - replacing null values
# replaced_df1 = df.fillna(value="unspecified")
# replaced_df2 = df.fillna(value="unspecified", inplace=True)  # replaces the value and returns Nane
# print(replaced_df1)
# print(replaced_df2)  # Nane

# replacing empty cells of the specified column
# df['Age'] = df['Age'].fillna('AGE')
# df['Cabin'] = df['Cabin'].fillna('CABIN')

# replacing empty cells with mean, median and mode
# target columns:- Age, Cabin
mean = df['Age'].mean()   # mean = 29.69911764705882
median = df['Fare'].median()  # median = 14.4542
mode = df['Cabin'].mode()[0]   # mode = B96 B98

df['Age'] = df['Age'].fillna(value=mean)  # notice row 888 - the value must be : 29.699118
df['Cabin'] = df['Cabin'].fillna(value=mode)  # notice row 0,2,4,...,886,888,890 - value : B96 B98
df['Fare'] = df['Fare'].fillna(value=median)  # notice row 887 - value : 14.4542
print(df.to_string())
