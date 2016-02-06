'''
problem_1_4.py
CMPS101 Winter 2016


This program was written by:
Seth Larkin: sslarkin@ucsc.edu
and
Abraham Chavez: achave11@ucsc.edu

Description: A program to plot best/worst case for insertion-sort and merge-sort
algorithms.

Program status: 
compiles, runs
'''

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import timeit
import scipy

import problem_1_3 as prog3

'''
plt.plot(prog3.BestInsert)
plt.plot(prog3.WorstInsert)
plt.xlabel("N Inputs")
plt.ylabel("Execution Time")
plt.title("InsertionSort (Green = worst-case, Blue = best)")
'''

plt.plot(prog3.BestMerge)                                                                                 
plt.plot(prog3.WorstMerge)                                                                                
plt.xlabel("N Inputs")
plt.ylabel("Execution Time")
plt.title("MergeSort (Green = worst-case, Blue = best)")
plt.show()
plt.plot(prog3.BestMerge)
plt.show(prog3.WorstMerge)

