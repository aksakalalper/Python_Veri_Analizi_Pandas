import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)
index=['a','b','c','d','e']
columns=['column1','column2','column3']
df=pd.DataFrame(data=data,index=index,columns=columns)
df=df.reindex(['a','b','c','d','x','e','f']) #fazladan index eklenince NAN hatasi veriyor.
df=df.isnull() #NAN degerleri bulur
print(df)
df=df.notnull() #NAN olmayanlari bulur
print(df)
df=df.drop(["x","f"],axis=0) #satir silinme metodu
print(df)
df=df.drop("column2",axis=1) #sutun silme metodu
print(df)
df=pd.DataFrame(data=data,index=index,columns=columns)
newColumn=[np.nan,30,np.nan,41,23] #yeni kolon eklendi
df["column4"]=newColumn
print(df)
print(df[df.notnull()]) #NAN olmayanlar cikti olarak geldi.
df=df.dropna() #NAN degerlerin oldugu satirlari getirmez
print(df)
df=pd.DataFrame(data=data,index=index,columns=columns)
df=df.dropna(thresh=2) #en az 2 sayida normal veri
df=pd.DataFrame(data=data,index=index,columns=columns)
df["column4"]=newColumn
df=df.fillna(value='no input') #NAN degerlere no input yazdirdik.
print(df)
