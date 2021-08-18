import time,multiprocessing
def findsquare(getlist):
    for i in getlist:
        time.sleep(5)#it will delay the process
        print(i*i)
def findcube(getlist):
    for i in getlist:
        time.sleep(3)
        print(i*i*i)
mylist=[2,3,4,5]
p1=multiprocessing.(target=findsquare,args=(mylist,))
p2=multiprocessing.(target=findcube,args=(mylist,))
p1.start()
p2.start()
p1.join()
p2.join()
print("......")
