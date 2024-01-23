def mergeSort(Arr):
	if len(Arr)> 1:
		mid = len(Arr)//2
		L = Arr[:mid]
		R = Arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] <= R[i]:
				Arr[k] = L[i]
				i+=1
				k+=1
			else:
				Arr[k] = R[j]
				j+=1
				k+=1
			
		while i<len(L):
			Arr[k] = L[i]
			i+=1
			k+=1

		while j<len(R):
			Arr[k] = R[j]
			j+=1
			k+=1
		print(Arr)





# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

# def mergeOrderList(ListA,ListB):
# 	newList = list()
# 	a= 0
# 	b = 0
# 	while a <len(ListA) and b < len(ListB):
# 		newList.append(ListA[a])
# 		a+=1
# 	else:
# 		newList.append(ListB[b])
# 		b+=1
# 	while a<len(ListA):
# 		newList.append(ListA[a])
# 		a+=1
# 	while b<len(ListB):
# 		newList.append(ListB[b])
# 		b+=1
# 	return newList
	


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	# print("Given array is")
	# printList(arr)
	mergeSort(arr)
	print("\nSorted array is ")
	printList(arr)
	print(5//2)
	print(arr[:])

# This code is contributed by Mayank Khanna
