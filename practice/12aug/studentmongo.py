import re,pymongo,logging
studentlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['StudentssssDb']
collection_name=mydatabase['students']
class StudentDetails:
    def init(self,name,rollno,clss,english,maths,social,science):
        self.name=name
        self.rollno=rollno
        self.clss=clss
        self.english=english
        self.maths=maths
        self.social=social
        self.science=science
    def addstudentdetail(self,name,rollno,clss,english,maths,social,science):
        totalmarks=int(english)+int(maths)+int(social)+int(science)
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"class":clss,"english":english,"maths":maths,"social":social,"science":science,"delflag":0} 
        studentlist.append(dict1)
obj=StudentDetails()        
while True:
    print("1.Add students with marks")
    print("2.View students with marks")
    print("3.Search a student")
    print("4.update a data")
    print("5.avg marks on english based on class") 
    print("6.delete a student")
    print("7.exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        name=input("Enter the name : ")
        rollno=input("Enter the roll no : ")
        clss=input("Enter the class : ")
        english=input("Enter the marks of English : ")
        maths=input("Enter the marks of maths : ")
        science=input("Enter the marks of Science : ")
        social=input("Enter the marks of Social : ")
        obj.addstudentdetail(name,rollno,clss,english,maths,social,science)
        result=collection_name.insert_many(studentlist)
        print(result.inserted_ids)
    if choice==2:
        result=collection_name.find({"delflag":0},{"_id":0})
        for i in result:
            studentlist.append(i)
            print(i)
    if choice==3:
        name=input("enter the class")
        roll=input("enter the roll no")
        # result=collection_name.aggregate([{ '$match':{'$and':[{"section":name},{"rollno":roll}]}}])
        result=collection_name.find({"$and":[{"class":name},{"rollno":roll},{"delflag":0}]})
        for i in result:
            print(i)
    if choice==4:
        c=input("enter the class")
        r=input("enter the rollno")
        m=input("enter the marks to be updated")
        result= collection_name.update_one({"$and":[{"class":c},{"rollno":r}]},{"$set":{"maths": m }})
        print(result)
    if choice==5:
        result=collection_name.aggregate([{"$group":{"average":{"$avg":{"$toDouble":"$english"}}}}])
        for i in result:
            print(i)
    if choice==6:
        s=input("enter the class") 
        v=input("enter the rollno")
        result=collection_name.update_one({"$and":[{"class":s},{"rollno":v}]},{"$set":{"delflag":1}}) 
        print(result)
    if choice==7:
        break
        
        