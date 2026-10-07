def quickSort(arr,start,end):
    if start<end:
        index = partition(arr,start,end)
        quickSort(arr,start,index-1)
        quickSort(arr,index+1,end)
def partition(arr,start,end):

    pivot = arr[start]
    i=start+1
    j= end
    while i<j:
        while i<end and arr[i]<=pivot:
            i+=1
        while j>start and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[start],arr[j]=arr[j],arr[start]

    return j
arr=[10,16,8,12,15,6,3,9]
quickSort(arr,0,len(arr)-1)
print("Sorted array: ",arr)
