import re
def valimodule(name,rollno,admno,mobile_number,emailId):
    val1=re.search('[A-Za-z],{2,25}\s[A-Za-z]{2,25}',name)
    val2=re.search("^[0-9]{2}",rollno)
    val3=re.search("[0-9]{0,9}$",admno)
    val4=re.search("(0|91)?[7-9][0-9]{9}",mobile_number)
    val5=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w[2,3]$",emailId)
    if val1 and val2 and val3 and val4 and val5:
        return True
    else:
        return False