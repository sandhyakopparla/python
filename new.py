import csv
headerContent=["Name","Roll"]

studentData=[
    {"Name":"Annu","Roll":22},
    {"Name":"arun","Roll":21},
    {"Name":"Amith","Roll":23},
    {"Name":"akash","Roll":3},
    {"Name":"Aswin","Roll":2},
]
with open('student.csv','w+',encoding='UTF8',newline='') as s:
    writer=csv.DictWriter(s,fieldnames=headerContent)
    writer.writeheader()
    writer.writerows(studentData)



