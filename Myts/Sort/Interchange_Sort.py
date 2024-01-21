Arr = [8, 4, 1, 6, 5,10000]

for i in range(len(Arr)):
    for j in range(i+1, len(Arr)):
        temp = Arr[i]
        if Arr[i] > Arr[j]:
            Arr[i] = Arr[j]
            Arr[j] = temp

print(Arr)


a ="sadbutsad"
print(a[0:8])