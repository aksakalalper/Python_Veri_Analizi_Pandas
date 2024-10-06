import pandas as pd
import numpy as np

df=pd.read_csv("all_seasons.csv") #csv dosyası okundu
print(df)
df=pd.read_json("file.json") #json dosyasi okundu.
print(df)
df=pd.read_excel("book.xlsx") #excel dosyasi okundu.
print(df)