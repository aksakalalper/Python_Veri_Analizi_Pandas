import pandas as pd
import numpy as np

file="book.xlsx"
data=pd.read_excel(file)
df=pd.DataFrame(data=data)
print(df)
result=df.groupby("Departman").groups #gruplama yapildi.
print(result)
print("----------------")
result=df.groupby(["Departman","Semt"]).groups #hem departman hem semtleri ayni olan indeksler gruplandi.
print(result)
print("..........................")
semtler=df.groupby("Semt")
for name,group in semtler: #semt kolonu icindeki isimleri tek tek yazdirip indeksleri ekrana basar.
    print(name)
    print("*******")
    print(group)

result=df.groupby("Semt").get_group("Tuzla") #tuzla semtinde calisanlar geldi
print(result)
result=df.groupby("Semt")["Maaş"].sum() #semtlere gore maas toplamlari geldi
print(result)
result=df.groupby("Departman")["Yaş"].mean() 
print(result)
result=df.groupby("Departman")["Yaş"].mean()["Finans"]
print(result)
result=df.groupby("Departman")["Yaş"].agg(np.mean)
print(result)
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.min,np.max])
print(result)
