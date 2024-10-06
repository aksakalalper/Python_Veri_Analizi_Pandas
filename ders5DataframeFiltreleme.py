import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
column=["column1","column2","column3","column4","column5"]
df=pd.DataFrame(data=data,columns=column)
result=df.columns
print(result)
result=df.head(5) #en bas 5 index gelir.
print(result)
result=df.tail(5) #son 5 kayit gelir.
print(result)
result=df.column1.head(4) #column1 ilk 4 kaydi alinir.
print(result)
result=df[["column1","column2"]].head(5) #2 adet kolon alinir.
print(result)
result=(df>=20) #her elemani kontrol edil true yada false dondurur.
print(result)
result=(df[df>=20]) #degerleri de gosterip kontrol eder. butun kolonlarda.
print(result)
result=df[df["column1"]>=50][["column1"]] #kolon1 de kontrol edip onu secer.
print(result)
result=df[(df["column1"]>=60) & (df["column2"]>=60)][["column1","column2"]] #kolon1 ve kolon2 secilip kontrol eder.
print(result)
result=df.query("column1>=50 & column2>=70")[["column1","column2"]] #daha pratik yontem,s direkt sart yazilir.
print(result)

