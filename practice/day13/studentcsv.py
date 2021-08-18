import sys,re,csv
header =['total','name','rollno','admin','english','hindi','maths','science','social']
studentlist= []
# def val(rollno,admin,english,hindi,maths,science,social):
#     val=re.search("^[1-9]",rollno)
#     val1=re.search('^[1-9]',admin)
#     val2=re.search('^[0-9]',english)
#     val3=re.search('^[0-9]',maths)
#     val4=re.search('^[0-9]',social)
#     val5=re.search('^[0-9]',hindi)
#     val6=re.search('^[0-9]',science)
#     if val and val1 and val2 and val3 and val4 and val5 and val6:
#         return True
#     else:
#         return False
                # sys.exit()
class StudentData:
        def addstudentdetail(self,name,rollno,admin,english,hindi,maths,science,social):
            totalmarks=english+hindi+maths+science+social
            dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"hindi":hindi,"maths":maths,"science":science,"social":social}
            studentlist.append(dict1)
obj1=StudentData()
while(True):
    print("1. Add student details - ")
    print("2. Display student details Like API - ")
    print("3. Search student by Rollno - ")
    print("4. Ranking - ")
    print("5. Exit - ")
    print('6. save to file - ')
    choice = int(input('enter your choice - '))
    if choice==1:
        name = input("enter the name of student - ")
        rollno=int(input("enter the Rollno - "))
        admin=int(input('enter the admin no -  '))
        english=int(input("enter the english marks: "))
        social=int(input("enter the social marks:"))
        maths=int(input("enter the maths marks: "))
        hindi=int(input("enter the hindi marks: "))
        science=int(input("enter the science marks: "))
        x=val(rollno,admin,english,maths,social,hindi,science)
        if x:
            obj1.addstudentdetail(name,rollno,admin,english,hindi,maths,science,social)
        else:
            print("validation not done properly")
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=int(input("enter the rollno to search:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice == 4:
        print(sorted(studentlist,reverse=True,key=lambda i:i['total']))
    if choice == 6:
        with open('std.csv','w+',encoding='UTF8',newline='') as s:
            writer = csv.DictWriter(s,fieldnames=header)
            writer.writeheader()
            writer.writerows(studentlist)
    if choice==5:
        sys.exit()