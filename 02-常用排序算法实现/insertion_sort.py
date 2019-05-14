def insertSort(arr):
    if not arr:
        return 0
    
    for i in range(1,len(arr)):

        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


#test

arr = [5,3,6,9,2,8,6,9]

insertSort(arr)

print(arr)