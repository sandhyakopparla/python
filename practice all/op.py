import timeit
def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                arr[j+1] = key
arr = [12, 11, 13, 5, 6]
insertionsort(arr)
# print(timeit.timeit(insertionsort,number=1000))
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(timeit.timeit(insertionsort,number=1000))
print(timeit.timeit(bubbleSort,number=1000))
  

