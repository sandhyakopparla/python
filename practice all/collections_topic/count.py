from collections import Counter
a=[1,2,2,3,4,32,9,2,3,5,5,1]
count=Counter(a)
print(list(count.elements())) #it will print the output in an ordered format like 1,1,2,2,2
print(count)