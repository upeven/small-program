# __author__:乌龟攻城狮

def selectSort(arr):
    if not arr:
        return "空列表"
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]
    
    return arr

#test
A = [64, 25, 12, 22, 11] 
print(selectSort(A))
