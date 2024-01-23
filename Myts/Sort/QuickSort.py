#the main idea of quicksort is base on divide and conquer
# [10, 7, 8, 9, 1, 5] 
#we will find the median of the array which mean that all
#elements to left will smaller than median and all elements to the right
#will greater than it 

def partition(array, low, high):
	pivot = array[high] 

	i = low -1 
	for j in range(low,high):
		if array[j] <=pivot:
			i +=1
			array[i],array[j] = array[j],array[i]
	array[i+1],array[high]= array[high],array[i+1]#swap position of pivot
	
	return i+1
def quicksort(array,low,high):
	if low<high:
		pi = partition(array,low,high)
		quicksort(array,low,pi-1) #sort left side of pivot
		quicksort(array,pi+1,high) #sort right size of pivot

array = [10, 7, 8, 9, 1, 5]
N = len(array)

	# Function call
quicksort(array, 0, N - 1)
print('Sorted array:')
for x in array:
	print(x, end=" ")




def partition(array,low,high):
	pivot = array[high]
	i = low -1
	for j in range(low,high):
		if array[j] <= pivot:
			i +=1									
			array[i],array[j] = array[j],array[i] # [10, 7, 8, 9, 1, 5] array[i] > pivot and array[j] < pivot => array[j] <array[i]
													#array[i] > array[j]
		array[i+1],array[high] = array[high],array[i+1] #array[i+1]  contain the element > pivot 
														#so we need to swap it 
def quicksort(array,low,high):
	if low < high:
		pi = partition(array,low,high)
		quicksort(array,low,pi-1) #sort left side
		quicksort(array,pi+1,high) #sort right side
