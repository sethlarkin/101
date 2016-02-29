

A = []

size = 0
total = 0
heap = False

root = 0
left= 0
right = 0

def parent(i):
    return(i//2)

def left(i):
    return(2*i)

def right(i):
    return(2*i+1)     

def swap(j, k):
    if (j < 1 and k < 1 and j <= size and k <= size):
        return
    temp = A[k]
    A[k] = A[j]
    A[j] = temp

def indexOfSmallest(i, left, right):        
    minIndex = i
    if (size >= left and A[left] < A[minIndex]):
        minIndex = left
    elif (size >= right and A[right] < A[minIndex]):
        minIndex = right
    return minIndex

def heapify(i):
    n = indexOfSmallest(i, left(i), right(i))
    if i != n:  
        swap(i,n)
        heapify(n)
    if i == size: #is now min
        return

def buildheap():
    for i in range(size/2, 1):
        print(i)

def insert(x):
    A.append(x)


insert(11)
insert(6)
insert(9)
insert(1)

print (A)
heapify(0)

print(size(A))

    
