# counting sort

def counting_sort(arr, n):
    newArr = [0] * (n+1)
    result = []

    for num in arr:                     # Count each number
        newArr[num]+=1
    
    for i in range(0, n + 1):           # Add numbers in sorted order
        count = newArr[i]
        while count > 0:
            result.append(i)
            count -= 1

    return(result)

arr = [5, 3, 2, 2, 5, 1, 4]
print(counting_sort(arr, len(arr)))    