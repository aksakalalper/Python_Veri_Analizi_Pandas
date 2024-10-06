import pandas as pd
import numpy as np

file="imdb250.csv"
data=pd.read_csv(file)
df=pd.DataFrame(data=data)
print(df)
print(df.groupby(["name","year"]).groups)
movies=df.groupby("directors")

for directors,group in movies:
    print(directors,group)
    
print(df.loc[234])
print(df.groupby("name").get_group("My Father and My Son"))