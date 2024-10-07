import pandas as pd

data={
    'column1':[1,2,6,4,5],
    'column2':[10,20,30,20,50],
    'column3':['aa','bb','cc','dd','ee']
}

def kareAlma(x):
    return x*x

df=pd.DataFrame(data=data)
print(df,"\n***************************************")
result=df['column2'].unique() #sadece 1 kere yazilan bilgiler gelir.
print(result,"\n***************************************")
result=df['column2'].nunique() #sadece 1 kere yazilan bilgilerin adetini verir.
print(result,"\n***************************************")
result=df['column2'].value_counts() #elemanlarin adetini verir.
print(result,"\n***************************************")
result=df['column2'].apply(kareAlma) #kolonu fonksiyona gondermek icin apply fonk. kullanilir.
print(result,"\n***************************************")
df['column4']=[12,13,15,10,4]
result2=df.sort_values("column4",ascending=False)["column4"] #belirli bir kolonu filtreleyerek azalan siralama yaptik.
print(result2,"----------------------")
result2=df.sort_values("column4",ascending=True)["column4"] #belirli bir kolonu filtreleyerek artan siralama yaptik.
print(result2,"----------------------")

data={
    'ay':["mayıs","haziran","nisan","mayıs","haziran","nisan","mayıs","haziran","nisan"],
    'kategori':["elektronik","elektronik","elektronik","kitap","kitap","kitap","giyim","giyim","giyim"],
    'gelir':[20,30,15,14,32,42,12,36,52]

}
df1=pd.DataFrame(data=data)
print(df1,"\n************************")
dfPivot=pd.pivot_table(data=df1,index="ay",columns="kategori",values="gelir") #veriler pivot tablo haline geitrildi.
print(dfPivot)

