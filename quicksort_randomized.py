import random

def quicksort(arr, start , stop):
	if(start < stop):
		
		pivotindex = partitionrand(arr,start, stop)
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

def partitionrand(arr , start, stop):
	randpivot = random.randrange(start, stop)
	arr[start], arr[randpivot] = arr[randpivot], arr[start]
	return partition(arr, start, stop)

def partition(arr,start,stop):
	pivot = start # pivot
	i = start + 1
	for j in range(start + 1, stop + 1):

		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] =arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

if __name__ == "__main__":
	lst=[]
	n = int(input("Enter number of elements : "))

	for i in range(0, n):
		ele = int(input())
		lst.append(ele) 
	size = len(lst)
	quicksort(lst, 0, size - 1)
	print(lst)

