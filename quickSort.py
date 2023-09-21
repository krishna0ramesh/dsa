def partition(arr,start,end):
    
    l=start
    r=end-1 #end element is pivot

    while l<r:
        # Increment left pointer if number is less or equal to pivot
        if arr[l]<=arr[end]:
            l+=1 
        # Decrement right pointer if number is greater to pivot
        elif arr[r]>arr[end]:
            r-=1 
        else:
            arr[l],arr[r]=arr[r],arr[l]
    
    if arr[l]>arr[end]:
        arr[l],arr[end]=arr[end],arr[l]
        return l
    else:
        return end

def quickSort(arr,start=0,end=None):

    if end is None:
        end=len(arr)-1
    if start<end:
        pivotPosition=partition(arr,start,end) 
        quickSort(arr,start,pivotPosition-1)
        quickSort(arr,pivotPosition+1,end)
    return arr

n=int(input("Enter the number of elements"))
print("Enter the elements")
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

result=[]
result=quickSort(arr)
print(result)