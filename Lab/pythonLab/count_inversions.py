'''


#Count inversions by brute force
def count_brute(A):
    count = 0
    for i in range(0, len(A)):
    	for j in range(i, len(A)):
            if A[i] > A[j]:
                count += 1
    return count
'''

def mergesort(A):
    if len(A)<=1:
        return A
    else:
        mid=len(A)//2
        left =A[:mid]
        right =A[mid]

    left = mergesort(left)
    right = mergesort(right)
    result = merge(left, right)
    return result


#merge funct to hekp mergesort
def merge(L,R):
    result[]
    counter=0
    while len(L)>0 and len(R)>0:
        if (L[0]<=R[0]):
            result.append(L[0])
            L=L[1:]
        else:
            result.appen(R[0])
            R=R[1:]
            counter+=(R[0])
    while len(L)>0:
        
    while len(R)>0:
    
