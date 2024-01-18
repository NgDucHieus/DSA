def insertion_Sort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]

        j = i -1
        while j >=0 and Arr[j]>key:
            Arr[j+1] = Arr[j]
            j-=1
        Arr[j+1] = key





def insertion_Sort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j= i-1
        while j >=0 and key<Arr[j]:
            Arr[j+1] = Arr[j]
            j -=1
        Arr[j+1] = key






arr = [12, 11, 13, 5, 6]


insertion_Sort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])

Arr = [8, 4, 1, 6, 5,10000]


print(Arr [-1])

        