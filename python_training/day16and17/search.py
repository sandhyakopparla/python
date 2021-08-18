import pymongo
mydatabase=client['EmployeeDb']
collection_name=mydatabase['students']
result=collection_name.find({"name":sandhya},{"_id":0})
employeelist=[]
for i in result:
    employeelist.append(i)
print(employeelist)