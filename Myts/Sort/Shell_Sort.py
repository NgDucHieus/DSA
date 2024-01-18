def Shell_sort(Arr):
    gap = len(Arr)//2
    while gap > 0:
        j= gap 
        while j < len(Arr):
            i = j -gap

            while i >= 0:
                if Arr[i+gap] > Arr[i]:
                    break
                else:
                    Arr[i+gap],Arr[i] = Arr[i],Arr[i+gap]
                i = i -gap
            j+=1
        gap= gap //2
arr2 = [12, 34, 54, 2, 3] 
Shell_sort(arr2)
print(arr2)