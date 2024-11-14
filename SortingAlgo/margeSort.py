
def marge(arr, left,mid,right):
    n1 = mid - left + 1
    n2 = right - mid

    arrL = [0]*n1
    arrR = [0]*n2

    for i in range(n1):
        arrL[i] = arr[left+i]
    for i in range(n2):
        arrR[i] = arr[mid+i+1]    
   
    i,j,k=0,0,left
    while i<n1 and j<n2:
        if arrL[i] <= arrR[j]:
            arr[k] = arrL[i]
            i+=1
        else:
            arr[k] = arrR[j]
            j+=1
        k+=1
    
    while i<n1:
        arr[k] = arrL[i]
        i+=1
        k+=1

    while j<n2:
        arr[k] = arrR[j]
        j+=1
        k+=1



def margeSort(arr,left,right):

    if left>=right:
        return
 
    mid = left+ (right-left)//2
    margeSort(arr,left,mid)
    margeSort(arr,mid+1,right)
    marge(arr,left,mid,right)




arr = [2,3,41,0,3,5,23,56,21,22,45,49,29]

n = len(arr)

margeSort(arr,0,n-1)

print("Sorted Array : ")
print(arr)