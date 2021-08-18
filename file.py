while (True):
    print("1.Add name")
    print("2.Display")
    print("3.Exit")
    choice=int(input("Enter your choice "))
    if choice==1:
        user=input("Enter the name : ")
        myfile=open('demo.txt','w+')
        myfile.write(user)
        
    if choice==2:
        myfile=open('demo.txt','r+')
        x=myfile.read()
        # print(str(x))
        print(x)
        myfile.close()
    if choice==3:
        break
