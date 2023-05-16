# DataFrame - a two dimensional array-like object, or tabulated structure with rows and columns

import pandas as pd
import numpy as np

# creating DataFrame from dictionaries

french_novelists = {
    "Gustave Flaubert": ["Madame Bovary", "Sentimental Education", "Salammbô"],
    "Victor Hugo": ["Les Misérables", "The Hunchback of Notre-Dame", "Les Travailleurs de la Mer"],
    "Albert Camus": ["The Stranger", "The Plague", "The Fall"],
    "Marcel Proust": ["In Search of Lost Time", "Swann's Way", "Within a Budding Grove"],
    "Émile Zola": ["Germinal", "Nana", "L'Assommoir"],
    "Françoise Sagan": ["Bonjour Tristesse", "A Certain Smile", "Those Without Shadows"],
    "Marguerite Duras": ["The Lover", "The Sea Wall", "Hiroshima Mon Amour"],
    "Gustave Flaubert": ["Madame Bovary", "Sentimental Education", "Salammbô"],
    "Colette": ["Gigi", "Chéri", "The Vagabond"],
    "Alexandre Dumas": ["The Three Musketeers", "The Count of Monte Cristo", "The Vicomte de Bragelonne"],
    "Jean-Paul Sartre": ["Nausea", "No Exit", "The Age of Reason"],
    "Voltaire": ["Candide", "Zadig", "Micromégas"]
}

novelist_df = pd.DataFrame(french_novelists)

# print(novelist_df)
# print(f"The shape of the given dataframe: {novelist_df.shape}")
# print(f"List of novelists only: \n {novelist_df.columns}")
# print(f"list of Books: \n {novelist_df.values}")

# Locating rows
# print(novelist_df.loc[1])   # this will return the second row as a series  -  [] returns series
# print(novelist_df.loc[[0]])   # this will return the first row as a dataframe  -  [[]] returns dataframe
 
# Naming indexes

novelist_df = pd.DataFrame(french_novelists, index=["Book1", "Book2", "Book3"])

# print(novelist_df)


# read data from csv

df_one = pd.read_csv("C:\\Users\\hp pavilion\\Documents\\Python\\Machine learning\\Python_libraries\\Pandas\\resources\\data.csv")

print(df_one)

df_two = pd.read_csv("C:\\Users\\hp pavilion\\Documents\\Python\\Machine learning\\Python_libraries\\Pandas\\resources\\Files\\data-master\\bad-drivers\\bad-drivers.csv")

print(df_two)