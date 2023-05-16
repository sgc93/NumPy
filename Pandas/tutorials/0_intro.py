# as introduction

import pandas as pd

# printing the version of the installed pandas library

version = pd.__version__
print(f"the version of the installed pandas is: {version}")

# printing Ethiopian novelists and their books an tabulated form 

sample_data = {
    "Bealu":["Hadis", "Oromay", "Yhilena Dewol"],
    "Alex":["Zubeyda", "keletat gimash ken", "Gash Ashebr BeAmerica"],
    "Alemayehu":["Tale", "Hasetegnaw", "YeBrihan Felegoch"],
    "Alemayehu Wase":["Zgora", "Emegua", "Merhibibet"]
}

framed_data = pd.DataFrame(sample_data)
print(framed_data)