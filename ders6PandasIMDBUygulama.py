import pandas as pd
import numpy as np

file="imdb250.csv"
#1 dosyayi okuyalim
df=pd.read_csv(file)
print(df)
print(df.index)
print(df.columns)
#2 ilk 5 kaydi gosterin.
print(df.head(5))
#3 son 5 kaydi gosterin.
print(df.tail(5))
#4 sadece film adi kolonunu alin.
print(df["name"])
#5 sadece film adi kolonunu iceren ilk 5 kaydi alin.
print(df["name"].head(5))
#6 film adi ve rating kolonunu iceren son 7 kaydi alin.
print(df[["rating","name"]].tail(7))
#7 film adi ve rating kolonunu iceren 5-10 arasi kayiti alin.
print(df[["rating","name"]][5:10])
#8 isim ve rating kolonunu iceren ve puani 8 ustu olan kayitlardan ilk 50 sini getiriniz.
print(df.query("rating>=8.0")[["rating","name"]].head(50))
#9 cikis tarihi 2014-2015 arasinda olan filmleri gosteriniz.
print(df.query("2014<=year<=2015"))
#10 aksiyon turlu ve puani 8 ustu olan filmleri bul
print(df.query("rating>=8.0  & genre=='Action' ")["name"])

