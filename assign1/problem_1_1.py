'''
problem_1_1.py
CMPS101 Winter 2016

This program was written by:
Seth Larkin: sslarkin@ucsc.edu
and
Abraham Chavez: achave11@ucsc.edu

Description: A program containing insertion-sort and merge-sort
algorithms.

Program status: 
compiles, runs
'''
import numpy as np

Infn= 10002

def insertionSort(a):
    for j in range(1,len(a)):
        key = a[j]
        i = j-1
        while i>-1 and a[i]>key:
            a[i+1]=a[i]
            i = i-1
        a[i+1]=key
    return a


#function for calling merge-sort
def MergeSort(Array):
    Frnt= 0
    Rear= Array.size-1
    Array = Mergent(Array,Frnt,Rear)
    return Array
#Merge-sort, folloing the sudo code in the text book
def Mergent(Array, Front, Rear):
    if Front < Rear:
        MidPoint = Rear +((Front-Rear)//2)
        Mergent(Array, Front, MidPoint)    
        Mergent(Array, MidPoint+1, Rear)
        Merge(Array, Front, MidPoint,Rear)  
        return Array         
#Merge, following sudo code in text book
def Merge(Array, Front, MidPoint, Rear):
    AnL = MidPoint- Front+1
    AnR = Rear - MidPoint
    L_Ar = np.zeros(AnL+1, int) 
    R_Ar = np.zeros(AnR+1, int)
    for i in np.arange(0, AnL):
        L_Ar[i] = Array[Front+i]
    for j in np.arange(0, AnR):
        R_Ar[j] = Array[MidPoint+j+1]    
    L_Ar[AnL] = Infn
    R_Ar[AnR] = Infn
    i = 0
    j = 0
    k = Front
    for k in np.arange(Front,Rear+1):
        if L_Ar[i] <= R_Ar[j]:
            Array[k] = L_Ar[i]
            i += 1
        elif R_Ar[j] <= L_Ar[i]:
            Array[k]= R_Ar[j]
            j += 1
        else: return

