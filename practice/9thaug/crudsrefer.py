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



        #**********choice1************
        obj=Product()
        obj.addproductdetails()
        print(productlist)
        result=collection_name.insert_many(productlist)
        print(result.inserted_ids)