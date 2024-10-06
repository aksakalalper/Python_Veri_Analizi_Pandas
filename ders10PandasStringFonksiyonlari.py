import pandas as pd
import numpy as np

data=pd.read_csv("imdb250.csv")
data["writers"]=data["writers"].str.upper() #string formatina cevrilerek hepsi buyuk yapildi.
print(data.head(5))
data["index"]=data["writers"].str.find("STEPHEN KING") #yazarlar string formatina cevrilerek arandi.
print(data[["name","index"]][:50])
print(data[["name","index"]][50:100])
print(data[["name","index"]][100:150])
print(data[["name","index"]][150:200])
print(data[["name","index"]][200:250])
