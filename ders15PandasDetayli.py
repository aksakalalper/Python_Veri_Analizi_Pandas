import numpy as np
import pandas as pd

list=[1,2,4,54,78],[4,5,7,6,9]
list1=np.array(list).reshape(2,5)
columns=["a","b","c","d","e"]
df=pd.DataFrame(list1,columns=columns)
print(df.sum()) #her satirin toplami yazdirilir.

file="engine_data.csv"
data=pd.read_csv(file)
df=pd.DataFrame(data)
print(df)
print(df.columns,df.shape,df.size,df.describe(),df.info()) #ozellikleri yazdirilir.
unique_elements = df['Failure Type'].unique()

print(f"'Sütun1'deki benzersiz elemanlar: {unique_elements}") #benzersiz elemanlar bulunur.
print(df.groupby("Failure Type").get_group("No Failure")) #hic hata olmayan indexler getiriliri.

