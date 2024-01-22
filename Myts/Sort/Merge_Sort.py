def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2

		L = arr[:mid]

		R = arr[mid:]

		mergeSort(L)

		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()
def mergeOrderList(ListA,ListB):
	newList = list()
	a= 0
	b = 0
	while a <len(ListA) and b < len(ListB):
		newList.append(ListA[a])
		a+=1
	else:
		newList.append(ListB[b])
		b+=1
	while a<len(ListA):
		newList.append(ListA[a])
		a+=1
	while b<len(ListB):
		newList.append(ListB[b])
		b+=1
	return newList
	

def mergeSort(Arr):
	if len(Arr) <= 1:
		return Arr
	else:
		mid = len(Arr)//2
		leftHalf = mergeSort(Arr[:mid])
		rightHalf = mergeSort(Arr[mid:])


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is")
	printList(arr)
	mergeSort(arr)
	print("\nSorted array is ")
	printList(arr)

# This code is contributed by Mayank Khanna
