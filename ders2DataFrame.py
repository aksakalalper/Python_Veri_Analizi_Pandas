#farkli serilerin toplamı dataframe'dir.
import pandas as pd
import numpy as np

s1=pd.Series([3,2,1,0]) #seri 1 olusturuldu.
s2=pd.Series([4,12,41,10]) #seri 2 olusturuldu.

data=dict(apples=s1,oranges=s2) #sozluk veri yapisinda birlestirildiler.
df=pd.DataFrame(data=data) #dataframe formatinda cikti alinir.
print(df)

data=[['ahmet',180],['mehmet',170],['ayse',150],['fatma',160]] 
df1=pd.DataFrame(data=data,columns=['Name','Height'],index=['Person1','Person2','Person3','Person4'])
print(df1) 

data2={'Name':['ahmet','mehmet','ayse','fatma'],'Grade':[50,60,70,80]}
data3=[
    {'Name':'ahmet','Value':18},
    {'Name':'ahmet','Value':18},
    {'Name':'ahmet','Value':18},
    {'Name':'ahmet','Value':18}
]
index=['person1','person2','person3','person4']
df2=pd.DataFrame(data=data2,index=index)
print(df2)
df3=pd.DataFrame(data=data3,index=index)
print(df3)
