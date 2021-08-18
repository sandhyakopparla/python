def addstudentdetails(self,name,rollno,admno,college,parent_name,mobile_number,emeilId)
    dict1={"name":name,"rollno":rollno,"admno":admno,"college":college,"parent_name":parent_name,"mobile_number":mobile_number,"emailId":emailId}
    studentlist.append(dict1)
class Marks(Student):
    def addmarksdetails(self,social,maths,hindi,science,english)
    totalmarks=social+maths+hindi+science+english
    dict2={"total":totalmarks,"social":social,"maths":maths,"hindi":hindi,"science":science,"english":english}
    studentlist.append(dict2)