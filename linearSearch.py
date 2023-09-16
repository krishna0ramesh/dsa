"""QUESTION:Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the 
            sum of all elements to the left is equal to the sum of all elements to the right."""

def balancedSum(numbers):
    totalSum=sum(numbers)
    leftSum=0
    for n in numbers:
            if leftSum==totalSum - n - leftSum:
                  return "YES"
            leftSum+=n
    return "NO"

n=int(input("Enter the no of elements:"))
lst=[]

print("Enter the elements")
for _ in range(n):
      i=int(input())
      lst.append(i)

result=balancedSum(lst)
print(result)

      
