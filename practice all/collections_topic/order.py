from collections import OrderedDict
d=OrderedDict()
d[1]='e'
d[2]='d'
d[3]='u'
d[4]='r'
print(d)
print(d.keys())#it is useful for know the keys
print(d.items())#it is useful for printing the items
d[1]='p'  #here we can change the value 
print(d)