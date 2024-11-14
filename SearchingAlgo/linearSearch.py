
def linearSearch(arr,itm):
    n = len(arr)
    for i in arr:
        if i == itm:
         return "Item is exit in array"
        
    return "Item is not exit in array"
  

arr = [2,3,41,0,3,5,23,56,21,22,45,49,29]
print("Enter an Element:")
itm = int(input())
print(linearSearch(arr,itm))
