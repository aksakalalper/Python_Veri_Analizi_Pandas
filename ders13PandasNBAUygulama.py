import pandas as pd
import numpy as np

file="all_seasons.csv"
data=pd.read_csv(file)
df=pd.DataFrame(data=data)
print(df,"\n***********************")

#1 ilk 10 kaydi getiriniz.
print(df.head(10),"\n***********************")

#2 toplam kac kayit vardir?
print(df.count(1),"\n***********************")

#3 tum oyuncularin boy ortalamasi nedir?
print(df["player_height"].mean(),"\n***********************")

#4 en uzun boy kimindir ve bu boy kactir?
print(df[["player_height","player_name"]].max(),"\n***********************")

#5 yasi 20-25 arasinda olan oyuncularin isimleri ve takimlari nelerdir?
print(df.query("20<=age<=25")[["player_name","team_abbreviation"]])

#6 john holland hangi takimda oynar?
result=df[df["player_name"]=='John Holland'][["team_abbreviation","player_name"]]
print(result,"\n***********************")

#7 takimlara gore oyuncularin ortalama boy bilgisi nedir?
result=df.groupby("team_abbreviation")["player_height"].agg(np.mean)
print(result,"\n***********************")

#8 kac farkli takim var?
result=df["team_abbreviation"].nunique()
print(result,"\n***********************")

#9 her takimda kac oyuncu oynamaktadir?
result=df.groupby("team_abbreviation").groups
list1=list(result.keys())
list2=list(result.values())
listMix=dict(zip(list1, list2))
value_counts = {}
for key, values in listMix.items():
    value_counts[key] = len(values)

print(value_counts)
