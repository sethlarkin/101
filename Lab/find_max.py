import numpy as np

def find_max(A, begin, end):
      if end - begin == 2:
          return max(A[begin], A[end-1])
      if end - begin == 1:
          return A[begin]
      mid = begin + (end - begin)//2
      print("beg ", begin)
      print("mid ", mid)
      print("end ", end)
      
      return max(find_max(A, begin, mid+1), find_max(A, mid, end))

A = np.random.rand(20)
print (find_max(A, 0, 20))
print(A)
print(A[len(A)//2])
