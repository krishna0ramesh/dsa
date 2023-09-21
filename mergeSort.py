def merge(left,right):

    result=[]
    i,j=0,0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    # Get the remaining parts and merge it to the result
    return result+left[i:]+right[j:]

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2

    left=arr[:mid]
    right=arr[mid:]

    leftSort=mergeSort(left)
    rightSort=mergeSort(right)


    sortedArr=merge(leftSort,rightSort)
    return sortedArr

n=int(input("Enter the number of elements"))
print("Enter the elements")
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

result=[]
result=mergeSort(arr)
print(result)