import re,sys,smtplib,logging,csv,json
from validate import valimodule
from collections import deque
header=["name","rollno","admno","college","parent_name","mobile_number","emailId","social","english","science","maths","telugu"]
studentlist=[]
class Student:
    def __init__(self,name,rollno,admno,college,parent_name,mobile_number,emailId):
        self.name=name
        self.rollno=rollno
        self.admno=admno
        self.college=college
        self.parent_name=parent_name
        self.mobile_number=mobile_number
        self.emailId=emailId
class Semresult(Student):
    def __init__(self,name,rollno,admno,college,parent_name,mobile_number,emailId,social,english,science,maths,telugu):
        self.social=social
        self.english=english
        self.science=science
        self.maths=maths 
        self.telugu=telugu
        super().__init__(name,rollno,admno,college,parent_name,mobile_number,emailId)
    def adddetails(self):
        totalmarks=int(social+english+science+maths+telugu)
        percentage=(totalmarks/200)*100
        dict1={"totalmarks":totalmarks,'name':name,'rollno':rollno,'admno':admno,'college':college,'parent_name':parent_name,'mobile_number':mobile_number,'emailId':emailId,'social':social,'english':english,'science':science,'maths':maths,'telugu':telugu}
        studentlist.append(dict1)
        print(studentlist)
while(True):
    print("\n enter your choice")
    print("1.Add student details with marks:")
    print("2.view all the student details with marks:")
    print("3.view all the student details based on the marks:")
    print("4.send an email to parents:")
    print("5.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        name=input("Enter the name : ")
        rollno=input("Enter the roll no : ")
        admno=input("Enter the admission no : ")
        college=input("enter the college name :")
        parent_name=input("enter the parent_name : ")
        mobile_number=input("enter the number : ")
        emailId=input("enter the email_id :")
        social=input("Enter the marks of social : ")
        english=input("Enter the marks of english : ")
        science=input("Enter the marks of Science : ")
        maths=input("Enter the marks of maths : ")
        telugu=input("Enter the marks of telugu : ")
        if valimodule(name,rollno,admno,mobile_number,emailId)==True:
            obj1=Semresult(name,rollno,admno,college,parent_name,mobile_number,emailId,social,english,science,maths,telugu)
            t=obj1.adddetails()
    if choice==2:
        with open('student2.csv','w+',encoding='UTF8',newline='') as s:
            writer = csv.DictWriter(s,fieldnames=header)
            writer.writeheader()
            writer.writerows(studentlist)
        myfile='student2.csv'
        jsonfilePath='student2.json'
        studentlist=[]
        with open(myfile,'r',encoding='utf-8') as f:
            dataReader=csv.DictReader(f)
            for data in dataReader:
                studentlist.append(data)
        studentlist_json=json.dumps(studentlist)
        with open(jsonfilePath,'w',encoding='utf-8') as f:
            f.write(studentlist_json)
    if choice==3:
        
        















 