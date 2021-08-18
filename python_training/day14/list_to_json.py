# import json
# studentlist=[{"name":"anuj","roll":23},{"name":"sidd","roll":13}]
# print(json.dumps(studentlist)) #if we want to convert anything into json then we have to use this method

import json
studentlist=[{"name":"anuj","roll":23},{"name":"sidd","roll":13}]
myjsondata=json.dumps(studentlist)
with open('test.json','w',encoding='utf-8') as f:
    f.write(myjsondata)

