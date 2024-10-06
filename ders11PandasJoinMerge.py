import pandas as pd

customers={
    'customerID':[1,2,3,4],
    'customerName':["ahmet","ali","ayse","fatma"],
    'customerLastName':["yilmaz","kuru","yay","yoru"]
}

orders={
    'orderID':[10,11,12,13],
    'customerID':[1,2,5,7],
    'orderDate':['2010-07-04','2010-08-04','2010-07-07','2014-02-05']
}
dfCustomers=pd.DataFrame(data=customers,columns=["customerID","customerName","customerLastName"])
dfOrders=pd.DataFrame(data=orders,columns=["orderID","customerID","orderDate"])

print(dfCustomers)
print(dfOrders)
result=pd.merge(dfCustomers,dfOrders,how="inner") #inner metodunda sadece ortak elemanlarin oldugu sekilde geliyor.
print(result)
result=pd.merge(dfCustomers,dfOrders,how="left") #left metodunda musteri df yi baz alir.
print(result)
result=pd.merge(dfCustomers,dfOrders,how="right") #right metodunda order df yi baz alir.
print(result)
result=pd.merge(dfCustomers,dfOrders,how="outer") #outer metodunda musteri ikisini baz alir.
print(result)

customersA={
    'customerID':[1,2,3,4],
    'customerName':["mehmet","ali","ayse","fatma"],
    'customerLastName':["yilmaz","ter","yay","yoru"]
}
customersB={
    'customerID':[1,2,3,4],
    'customerName':["yagmur","ali","ayse","fatma"],
    'customerLastName':["yilmaz","yas","yay","yoru"]
}

dfCustomersA=pd.DataFrame(customersA,columns=["customerID","customerName","customerLastName"])
dfCustomersB=pd.DataFrame(customersB,columns=["customerID","customerName","customerLastName"])

result=pd.concat([dfCustomers,dfCustomersB]) #alt alta yazdirdi
print(result)
result=pd.concat([dfCustomers,dfCustomersB],axis=1) #yanyana yazdirdi.
print(result)