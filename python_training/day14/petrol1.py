import csv,json,requests
f=open("petrol.json")
data=json.load(f)
for i in data:
    if i["rate"]<"70":
        print(i)