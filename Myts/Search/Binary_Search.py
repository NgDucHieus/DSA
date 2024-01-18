#recursive function
def rebinarySearch(Arr,l,r,x):
    #check the base case
    if l < r: 
        mid = l+(r - l) // 2 #calculate the location of the mid point

        #if element is present at the middle itself 
        if Arr[mid] == x: #best stiuation return mid
            return mid
        elif Arr[mid] < x: 
            return rebinarySearch(Arr,mid+1,r,x)
        else: return rebinarySearch(Arr,l,mid-1,x)

    #element is not present at the middle
    else: return -1



arr = [2,3,4,10,40]
x = 10
result = rebinarySearch(arr,0,len(arr)-1,x)
print(result)
