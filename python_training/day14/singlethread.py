import threading,time
# def printNumbers():
#     for i in range(1,10):
#         time.sleep(5)#it will delay the process
#         print(i)
# def printHello():
#     for i in range(1,3):
#         time.sleep(3)
#         print("Hello")

def findsquare(getlist):
    for i in getlist:
        time.sleep(5)#it will delay the process
        print(i*i)
def findcube(getlist):
    for i in getlist:
        time.sleep(3)
        print(i*i*i)
mylist=[2,3,4,5]
# t1=threading.Thread(target=printNumbers)
# t2=threading.Thread(target=printHello)
t1=threading.Thread(target=findsquare,args=(mylist,))
t2=threading.Thread(target=findcube,args=(mylist,))
t1.start()
t2.start()
t1.join()#after thread it will print "....."
t2.join()
print("........")
