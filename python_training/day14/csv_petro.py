import csv,json
myfile='petrol.csv'
jsonfilePath='petrol.json'
petrollist=[]
# ***Convert Csv to list
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.DictReader(f)

    for data in dataReader:
        petrollist.append(data)
#Convert list to Json
petrollist_json=json.dumps(petrollist)
with open(jsonfilePath,'w',encoding='utf-8') as f:
    f.write(petrollist_json)