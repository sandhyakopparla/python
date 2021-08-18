import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['Studen1Db']
collection_name=mydatabase['Students']
while(True):
    print("1.add students")
    print("2.search students")
    print("3.view the student count")
    print("4.delete")
    print("5.view del status")
    ch=int(input("enter the choice:"))
    if ch==1:
        name=input("enter the name")
        rollno=input("enter the roll no")
        branch=input("enter the branch")
        mydict={"name":name,"rollno":rollno,"branch":branch,"delflag":0}
        collection_name.insert_one(mydict)
    if ch==2:
        name=input("enter the name")
        result=collection_name.find({"$and":[{"name":name},{"delflag":0}]})
        # result=collection_name.find({"$or":[{"name":name},{"delflag":0}]})#it is for to satisfy either of one status
        for i in result:
            print(i)
    if ch==3:
        result=collection_name.aggregate([{"$group":{"_id":"$branch","no_of_students":{"$sum":1}}}])
        for i in result:
            print(i)
    if ch==4:
        rollno=input("enter the roll no to del")
        collection_name.update_one({"rollno":rollno},{"$set":{"delflag":1}})#delflag:0 means it is active,#if delflag:1 it shows the del status
    if ch==5:
        result=collection_name.find({"delflag":0})
        for i in result:
            print(i)                                                            
        