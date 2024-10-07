import pandas as pd
import numpy as np

file="GBvideos.csv"
data=pd.read_csv(file)
df=pd.DataFrame(data=data)
print(df.columns,df.index)

#1 ilk 10 kaydi getirin.
print(df.head(10))
#2 ikinci 10 kaydi getirin
print(df[10:20])
#3 datase icindeki kolon isimlerini ve sayisini bulun.
print(df.columns)
#4 thumnail_link,comments_disabled kolonlarini silip yeniden yazdirin.
print(df.drop(["thumbnail_link","comments_disabled"],axis=1))
#5 like ve dislike sutunlarının ortalamasini bulunuz.
print("like ortalamasi:",df["likes"].mean(),"dislike ortalamasi",df["dislikes"].mean())
#6 ilk 50 videonu likes ve dislikes kolonlarini getirin.
print(df[["title","dislikes","likes"]].head(50))
#7 en cok goruntulenen video hangisidir?
print(df[df["views"].max()==df["views"]][["title","views"]])
#8 en az goruntulenen video?
print(df[df["views"].min()==df["views"]][["title","views"]]) #1.metod
indeks=df[["views"]].idxmin() #2.metod
print(df.loc[indeks][["title","views"]])
#9 en fazla goruntulenen ilk 10 video hangisidir.
print(df.sort_values("views",ascending=False)[["views","title"]].head(10))
#10 kategoriye gore begeni ortalamalarini sirali sekilde getiriniz.
print(df.groupby("category_id")[["likes"]].agg(np.mean).sort_values("likes",ascending=False))
#11 her kategoride kac video vardir.
result=df.groupby("category_id").groups
list1=list(result.keys())
list2=list(result.values())
listMix=dict(zip(list1, list2))
value_counts = {}
for key, values in listMix.items():
    value_counts[key] = len(values)

print(value_counts)
#12 her videonun title uzunlugunu baska bir kolonda gosteriniz.
df["new"]=df["title"].str.len()
print(df["new"])
#13 her videoda kullanilan tag sayisini ayri bir kolonda gosteriniz.
df["new2"]=df["tags"].str.count("|")
print(df["new2"])