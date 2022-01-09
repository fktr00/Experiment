import pandas as pd
import os
current_directory = os.getcwd()
print(current_directory) 

df = pd.read_csv("/home/fktr0/Documents/GitHub/fktr00/experiment/JP/data/data.csv")
print(df)