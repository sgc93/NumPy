# series - is a one dimensional array-like object that can hold any data type at once.
import pandas as pd
import numpy as np

# creating a series of random data from a 2-D array

ethiopian_writers = np.array([["Dinaw Mengestu", "The Beautiful Things That Heaven Bears", "How to Read the Air"], ["Maaza Mengiste", "The Shadow King", "Beneath the Lion's Gaze"], ["Meron Hadero", "The Street Sweepers", "The Fire Never Goes Out"], ["Dagnachew Worku", "The Crown of Thorns", "Mysteries of the Horizon"], ["Mulugeta Alebachew", "The Blue Elephant", "The Crown of Solomon"], ["Tsegaye Gebre-Medhin", "The Thirteenth Sun", "Seth and the Two Wives"], ["Hama Tuma", "The Case of the Socialist Witchdoctor and Other Stories", "African Absurdities"], ["Befeqadu Hailu", "The Making of History: Chronicles of the Tigray People's Liberation Struggle", "On the Road with Cheetahs"], ["Bereket Habte Selassie", "The Crown and the Pen: The Memoirs of a Lawyer Turned Rebel", "What Was Communism?"], ["Tadelech Hailemikael", "Beneath the Lion's Gaze: A Novel of Ethiopia", "Gondar, Ethiopia: A Travel Guide"],
])

ethio_writers = pd.Series(ethiopian_writers.reshape(-1))
# print(ethio_writers)


# customizing keys of a series with index argument

ethiopian_foods = np.array(["Injera", "Doro Wat", "Tibs", "Kitfo", "Shiro", "Berbere", "Niter Kibbeh", "Ayib", "Firfir", "Kolo", "Enkulal Tibs", "Dulet", "Genfo", "Buticha", "Misir Wat", "Gomen", "Tekle Gomen", "Tere Sega", "Bozena Shiro", "Beyaynetu", "Dabo Kolo", "Ambasha", "Firfir", "Kita", "Kocho", "Kita"])

keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ethio_foods = pd.Series(ethiopian_foods, keys)
print(f"The list of some Ethiopian Foods: \n{ethio_foods}")


# Keys of a dictionaries as a Label
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

novelist_series = pd.Series(french_novelists)

# print(novelist_series)
