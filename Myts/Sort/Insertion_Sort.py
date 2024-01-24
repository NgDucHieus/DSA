def insertion_Sort(Arr): 
    for i in range(1,len(Arr)): 
        key = Arr[i] # i=1
        j = i -1    #j=0
        while j >=0 and Arr[j]>key: 
            Arr[j+1] = Arr[j]
            j-=1 #j =-1
        Arr[j+1] = key  
        print(Arr)
        



arr = [12, 11, 13, 5, 6]


insertion_Sort(arr)
# for i in range(len(arr)):
#     print ("% d" % arr[i])



# 

        