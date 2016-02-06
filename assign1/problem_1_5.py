
'''
problem_1_5.py
'''

import numpy as np
import timeit
import scipy
import matplotlib.pyplot as plt
from problem_1_1 import insertionSort, MergeSort


#Prepares Random array for insertion
def makeRandomArrayInsertion():
    b = np.zeros(1000, dtype=float)
    for i in range(1, 1000):
        np.random.seed(0)
        a = np.random.randint(10000, size=i)
        avg = getAverageInsertion(a)
        #print(avg)
        b[i] = avg    
    
    return b

#Gets average values of insertion
def getAverageInsertion(a):
    avgArray = np.zeros(1000, dtype=float)
    for j in range(0,1000):
        np.random.seed(0)
        np.random.permutation(a)
        t = timeit.Timer(lambda: insertionSort(a))
        avgArray[j] = scipy.mean(t.repeat(repeat=3,number=1))
    average = np.average(avgArray)
    return average            
    
#Prepares a random array for Merge
def makeRandomArrayMerge():
    b = np.zeros(1000, dtype=float)
    for i in range(1, 1000):
        np.random.seed(0)
        a = np.random.randint(10000, size=i)
        avg = getAverageMerge(a)
        b[i] = avg
    
    return b

#Gets average values from random Merge
def getAverageMerge(a):
    avgArray = np.zeros(1000, dtype=float)
    for j in range(0,1000):
        np.random.seed(0)
        np.random.permutation(a)
        t = timeit.Timer(lambda: MergeSort(a))
        avgArray[j] = scipy.mean(t.repeat(repeat=3,number=1))
    average = np.average(avgArray)
    return average

#Executes code to generate graph of median values
def main():
    plt.plot(makeRandomArrayInsertion())
    plt.xlabel("N Inputs")
    plt.ylabel("Execution Time")
    plt.title("InsertionSort (average case)")
    plt.figure(2)
    plt.plot(makeRandomArrayMerge())
    plt.xlabel("N Inputs")
    plt.ylabel("Execution Time")
    plt.title("MergeSort (average case)")
    plt.show()


main()
