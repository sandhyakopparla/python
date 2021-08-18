import csv,json
myfile='diesel.csv'
jsonfilePath='diesel.json'
diesellist=[]
# ***Convert Csv to list
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.DictReader(f)

    for data in dataReader:
        diesellist.append(data)
#Convert list to Json
diesellist_json=json.dumps(diesellist)
with open(jsonfilePath,'w',encoding='utf-8') as f:
    f.write(diesellist_json)