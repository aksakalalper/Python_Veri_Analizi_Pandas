import pandas as pd #buyuk data setleri uzerinden calisilir. csv,excel,db dosyalari uzerinde calisilir.
import numpy as np
#numpy dan farkli olarak her turlu heterojen data olabilir. numpy homojen olmak zorunda
#data
numbers=[1,2,3]
letters=['a','b','c']
mixed=['a','b','c',144]
dict={'a':1,'b':2,'c':3}
randomNumbers=np.random.randint(10,100,6)

pandasSeries=pd.Series(numbers) #her elemana bir index atanir.
print(pandasSeries)
pandasSeries=pd.Series(letters)
print(pandasSeries)
pandasSeries=pd.Series(mixed)
print(pandasSeries)
pandasSeries=pd.Series(10,numbers) #butun elemanlar on ile carpildi.
print(pandasSeries)
pandasSeries=pd.Series(numbers,letters) #letters listesi index olarak atandi.
print(pandasSeries)
pandasSeries=pd.Series(dict) #dictionary tipi de pandas a yuklenebilir.
print(pandasSeries)
pandasSeries=pd.Series(randomNumbers) #numpy dizisi de pandas series e eklenebilir.
print(pandasSeries)
pandasSeries=pd.Series(dict)
print(pandasSeries[['a','c']]) #farkli indeksleri cagirdik.
print(pandasSeries.ndim)
print(pandasSeries.sum()) #liste elemanlari toplandi.
print(pandasSeries>1) #liste elemanlari karsilastirildi.

hyundai2024=pd.Series([2000,4500,5500],['accent','elantra','tucson'])
hyundai2023=pd.Series([2000,3000,5500],['accent','elantra','i30'])

total=hyundai2023+hyundai2024
print(total)  #farkli key degerlerinde 'NAN' etiketi geri doner.
