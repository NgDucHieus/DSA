def heapify(arr,N,i):
    largest = i 
    l  = 2*i +1 # l == left
    r = 2*i + 1 #r == right

    if i < N and arr[largest] <arr[l]:
        largest = l 
    if i < N and arr[largest] < arr[r]:
        largest = r

    #change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        #Heapify the root
        heapify(arr,N,largest)
def heapSort(arr):
    N = len(arr)
    for i in range(N//2 -1,-1,-1):
        heapify(arr,N,i)
    for i in range(N-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr,i,0)