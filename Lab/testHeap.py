import math

A = []
root = 0
size = 0

def parent(i):
	if i > 0:
		if (i % 2 == 0):
			return (i//2-1)
		else:
			return i//2	
	else:
		return "root node"

def left(i):
	if (i <= len(A)/2):
		return 2 * i + 1
	else:
		return "leaf node"

def right(i):
	return 2 * i +2

def insert(x):
    A.append(x)
    global size
    size= size+1

def buildHeap():
	global size
	for i in range(size//2, 1, -1):
		heapify(i)

def heapify(i):
	global size
	n = indexOfSmallest(i, left(i), right(i))
	if (i != n):
		swap(i, n)
		heapify(n)
	if( i >= size):
		return

def indexOfSmallest(i, left, right):
	minIndex = i
	global size
	if (size >= left and A[left] < A[minIndex]):
		minIndex = left
	if (size >= right and A[right] < A[minIndex]):
		minIndex = right
	return minIndex

def swap(j, k):
    if (j < 1 and k < 1 and j <= size and k <= size):
        return
    temp = A[k]
    A[k] = A[j]
    A[j] = temp



print(size)
insert(1)
insert(4)
insert(6)
insert(5)
insert(12)

buildHeap()

print(A)
print("parent of A[3] ", A[3])
print ("is index", parent(3))

print ("left of A[2] is ", left(2))
print ("right of A[2] is ", right(2))


