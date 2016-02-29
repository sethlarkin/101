import timeit
import scipy

t = timeit.Timer("scipy.mean(range)")

print(t.timit(number=1))

