import pandas as pd
import numpy as np

data=np.random.randint(1,10,9).reshape(3,3) #3x3 luk matris olusturuldu
index=["a","b","c"]
columns=["column1","column2","column3"]
df=pd.DataFrame(data=data,index=index,columns=columns) #dataframe yaptik.
print(df)

result=df["column2"] #column2 yazdirildi.
print(result)

result=df[["column1","column3"]] #2 adet kolun secildi, yazdirildi. birden fazla kolon olunca dict veri yapisi ile cekilir.
print(result)

result=df.loc["a"] #a indeksi seri olarak yazdirir. kolon seklinde gelir gri donusu.
print(result)

result=df.loc['a','column2'] #a indeksinin column2 degeri yazdirilir.
print(result)

df["column4"]=pd.Series(np.random.randint(1,10,3),["a","b","c"]) #yeni kolon eklendi.
print(df)

df["column5"]=df["column2"]+df["column4"] #yeni kolon eklendi
print(df)
print("******")
df1=df.drop("column1",axis=1)
print(df1)
print("******")
print(df)