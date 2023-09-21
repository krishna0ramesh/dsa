def insertionSort(arr,n):
    for i in range(1,n):
        j=i
        while arr[j-1]>arr[j] and j>0: #checks whether numbers to the left is sorted
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    print(arr)

n=int(input("Enter the number of elements"))
print("Enter the elements")
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
insertionSort(arr,n)