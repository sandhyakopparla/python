import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['StudentDb']
collection_name=mydatabase['students']
getName=input('enter a name:')
getRoll=input('enter a Rollno:')
getCollege=input('enter a college name:')
data={"name":getName,"rollno":getRoll,"college":getCollege}
print(data)
collection_name.insert_one(data)
