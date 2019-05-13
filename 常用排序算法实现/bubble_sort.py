# 第一种实现
#__author__:，乌龟攻城狮

def bublleSort(arr):
    
    if not arr:
        return False
    
    for i in range(len(arr[:])):
        for j in range(i+1,len(arr[:])):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                continue

    return arr

# 第二种实现
def bubbleSort2(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a = [5,6,9,83,85,25,15]
print(bublleSort(a))
print(bubbleSort2(a))