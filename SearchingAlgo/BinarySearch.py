
def BinarySearch(arr,itm):
    l =0
    r = len(arr)-1

    while l<=r:
        mid = l + (r-l)//2

        if arr[mid]==itm:
            return "Item is exit in Array."
        elif arr[mid]<itm:
            l = mid +1
        elif arr[mid]>itm:
            r = mid - 1
    return "Item is not exit in Array."


arr = [2,3,41,0,3,5,23,56,21,22,45,49,29]
arr.sort()
print("Enter an Element:")
itm = int(input())
print(BinarySearch(arr,itm))