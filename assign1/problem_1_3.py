'''
problem_1_3.py
CMPS101 Winter 2016


This program was written by:
Seth Larkin: sslarkin@ucsc.edu
and
Abraham Chavez: achave11@ucsc.edu

Description: A program that

Program status: 
compiles, runs
'''
import numpy as np
import timeit
import scipy
import problem_1_1 as prg1

#make a reverse-order array: worst case for insertion-sort
def makeRevArray(size):
    a = np.zeros(size, dtype=int)
    j = a.size
    for i in range(0, a.size):
        a[i] = j
        j = j-1
    return a    

#make an in-order array: best case for insertion-sort
def makeArray(size):
    a = np.zeros(size, dtype=int)
    for i in range(0, a.size):
        a[i] = i+1
    return a     

#Create array which stores mergesort best time
def MergeBest(ValueT):
    timeAr = np.zeros(ValueT, dtype = float)
    for i in range(0, ValueT):
        Ar1 = makeArray(i)
        t = timeit.Timer(lambda: prg1.MergeSort(Ar1))
        timeAr[i] = scipy.mean((t.repeat(repeat=3, number=1)), dtype = float)
    return timeAr

#create an array which stores mergesort worst time
def MergeWorst(ValueT):
    timerAr = np.zeros(ValueT, dtype = float)
    for i in range(0, ValueT):
        Ar1 = makeRevArray(i)
        t = timeit.Timer(lambda: prg1.MergeSort(Ar1))
        timerAr[i] = scipy.mean((t.repeat(repeat=3, number=1)), dtype = float)
    return timerAr

#create array which stores the best time run in insertion
def InsertBest(ValueT):
    timerA = np.zeros(ValueT, dtype = float)
    
    for i in range(0, ValueT):
        Ar1 = makeArray(i)
        t = timeit.Timer(lambda: prg1.insertionSort(Ar1))
        timerA[i] = scipy.mean(t.repeat(repeat=3, number=1))
    return timerA

#create array which stored the worst time run for insertion sort
def InsertWorst(ValueT):
    timeAr = np.zeros(ValueT, dtype = float)
    
    for i in range(0, ValueT):
        Ar1 = makeRevArray(i)
        t = timeit.Timer(lambda: prg1.insertionSort(Ar1))
        timeAr[i] = scipy.mean(t.repeat(repeat=3, number=1))
    return timeAr

#Arrays for best and worst times for each merge and insertion sort 
BestInsert = InsertBest(1000)
WorstInsert = InsertWorst(1000)
BestMerge = MergeBest(1000)
WorstMerge = MergeWorst(1000)


