def bubbleSort(arr,n):
    for _ in range(n-1): #repeat process n-1 times

        for i in range(n-1): #iterate through elements except last element
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

    print(arr)

n=int(input("Enter the number of elements"))
print("Enter the elements")
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

bubbleSort(arr,n)

