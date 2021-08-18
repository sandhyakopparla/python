import csv,json
myfile='student.csv'
jsonfilePath='student.json'
studentlist=[]
# ***Convert Csv to list
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.DictReader(f)

    for data in dataReader:
        studentlist.append(data)
#Convert list to Json
studentlist_json=json.dumps(studentlist)
with open(jsonfilePath,'w',encoding='utf-8') as f:
    f.write(studentlist_json)


