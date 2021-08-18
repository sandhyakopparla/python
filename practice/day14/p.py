# try:
#     list = 5*[0]+5*[10]
#     x = list[9]
#     print(''Done!'')
# except IndexError:
#     print(''Index out of Bond! '')
# else:
#     print(''Nothing is wrong!'')
# finally:
#     print(''Finally block!'')

# class test: 
#     def __init__(self): 
#         print "Hello World" 

#     def __init__(self): 
#         print "Bye World" 

# obj=test()

# L = [3, 1, 2, 4]
# T = ('A', 'b', 'c', 'd')
# L.sort()
# counter = 0
# for x in T:
#     L[counter] += int(x)
#     counter += 1
#     break
# print(L)

# def __init__(self, name, age):
#     self.name = name
#     self.age = age  

L = list('123456')
L[0] = L[5] = 0
L[3] = L[-2]
print(L)