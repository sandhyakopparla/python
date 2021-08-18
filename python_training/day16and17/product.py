import re,sys,datetime,csv,time
from datetime import date
import pymongo
import time
productlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['ProductDb']
collection_name=mydatabase['products']
class Product:
    def addproductdetails(self):
        dict1={"productcode":productcode,"productname":productname,"distributor_name":distributor_name,"manufacturing_year":manufacturing_year,"retail_price":retail_price,"wholesale_price":wholesale_price,"product_discription":product_discription,"manufacturer_number":manufacturer_number}
        productlist.append(dict1)
while(True):
    print("1.Add Products")
    print("2.View all products")
    print("3.Search a product")
    choice=int(input("enter your choice:"))
    if choice==1:
        productcode=input("enter the productcode")
        productname=input("enter the product name")
        distributor_name=input("enter the distributor of product")
        manufacturing_year=input("enter year")
        retail_price=input("enter the retailprice")
        wholesale_price=input("enter the wholesale price")
        product_discription=input('enter the description')
        manufacturer_number=input("enter the number")
        obj=Product()
        obj.addproductdetails()
        print(productlist)
        result=collection_name.insert_many(productlist)
        print(result.inserted_ids)
    if choice==2:
        result=collection_name.find({},{"_id":0})
        productlist=[]
        for i in result:
            productlist.append(i)
        print(productlist)
    if choice==3:
        # result=collection_name.find({"productcode":"12"})
        # result=collection_name.find({"productname":{"$regex":"^S"}})
        # result=collection_name.find({"productname":{"$gt":"S"}})
        result=collection_name.delete_many({"productname":"Sandhya"})#for delete the particulator thing
        result=collection_name.update_one({"poductcode":"78"},{"$set":{"productname":"mamaearth"}})
        print(result)
        print(result.deleted_count)#to see how many deleted in the collections
        productlist=[]
        # for i in result:
        #     productlist.append(i)
        print(productlist)

    