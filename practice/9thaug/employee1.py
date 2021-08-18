# from collections import deque
import pymongo
import re,csv,sys,logging
from valiemploye import validation_of_employee
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['EmployeeDb']
collection_name=mydatabase['employees']
employeelist=[]
try:
    class Employee:
        def employeedetails(self,name,companyname,designation,salary,phone,address):
            self.name=name
            self.companyname=companyname
            self.designation=designation
            self.salary=salary
            self.phone=phone
            self.address=address 
        def addemployee(self):
            dict1={"name":name,"companyname":companyname,"designation":designation,"salary":salary,"phone":phone,"address":address}
            employeelist.append(dict1)
            obj1=Employee()
    while(True):
        print("1. AddEmp")
        print("2.view")
        print("3.Search a employee")
        print("5.update")
        print("4.delete")
        print("6.exit")
        choice=int(input("enter the choice"))
        if(choice==1):
            name=input("enter the name")
            companyname=input("enter the company name")
            designation=input("enter the designation")
            salary=input("enter the salary")
            phone=input("enter the number")
            address=input("enter the address")
            if validation_of_employee(name,phone,address):
                obj=Employee()
                obj.employeedetails(name,companyname,designation,salary,phone,address)
                obj.addemployee()
                print(employeelist)
                result=collection_name.insert_many(employeelist)
                print(result.inserted_ids) 
        if choice==2:
            #result=collection_name.find()
            # result=collection_name.find({},{"_id":0})
            result=collection_name.find({},{"_id":0})
            employeelist=[]
            for i in result:
                employeelist.append(i)
                print(employeelist)
        if choice==3:
            result=collection_name.find({"name":"anshu"})
            print(result)
            employeelist=[]
            for i in result:
                employeelist.append(i)
                print(employeelist)
        if choice==4:
            # result=collection_name.delete_one({"name":"karthik"}) 
            c=input("enter the companyname")
            result=collection_name.delete_one({"companyname":c}) 
            print(result)
        if choice==5:
            s=input("enter the salary")
            d=input("enter the designation:")
            result=collection_name.update_one({"salary":s},{"$set":{"designation":d}}) 
            print(result)
        if choice==6:
            sys.exit()
except:
    logging.error("Invalid validation kindly check it")
else:
    logging.info("done!")


        




        
    