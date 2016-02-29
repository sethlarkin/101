# Unit tests for Programming Assignment 2, CMPS101 Winter16 (Update 5)
# Copy this file to the folder where "assign2.py" is located
# ie. ucscid/assign2/hw2test.py

# If you implemented BONUS problem, uncomment line 48

import assign2 as p2
import numpy as np
import numpy.testing as nt
from scipy import linalg
import unittest
import os.path

class MyTest(unittest.TestCase):
    def test(self):
        nxn= [
            np.random.randint(-5,50,[2,2]),
            np.random.randint(-5,50,[4,4]),
            np.random.randint(-5,50,[8,8]),
            np.random.randint(-5,50,[16,16])
        ]
        had = [
            linalg.hadamard(2),
            linalg.hadamard(4),
            linalg.hadamard(8),
            linalg.hadamard(16)                   
        ]
        vec = [
            np.random.randint(-5,50,[2]),
            np.random.randint(-5,50,[4]),
            np.random.randint(-5,50,[8]),
            np.random.randint(-5,50,[16])
        ]
        for t in range(4):

            #Problem 1: matmult(A,x). Multiply a matrix with a vector.
            nt.assert_equal(p2.matmult(nxn[t],vec[t]),nxn[t].dot(vec[t]))

            #Problem 2: hadmat(k). Create hadamard of size 2^k
            # calls student hadmat with t=1,2,3,4
            # it is supposed to generate hadmat of size 2,4,8,16            
            nt.assert_equal(p2.hadmat(t+1),had[t])
            
            #Problem 4: hadmatmult(H,x). Takes hadamart H and vector x, multiplies.              
            nt.assert_equal(p2.hadmatmult(had[t],vec[t]),had[t].dot(vec[t]))
            
            #Bonus problem: efficienthadmatmult(x)
            #nt.assert_equal(p2.efficienthadmatmult(vec[t]),had[t].dot(vec[t]))
            
if __name__ == '__main__':

    #Assignment 2 file checks
    filesok=True
    if not os.path.isfile("README"):
        filesok=False        
        print("\nCANTFIND: README. If you have a readme file but still getting this error, check if it is upper case.\n")
    if not os.path.isfile("assign2.py"):
        filesok=False        
        print("\nCANTFIND: assign2.py. Make sure you name the python file correctly.\n")
    if not os.path.isfile("matmulttime.pdf"):
        filesok=False        
        print("\nCANTFIND: matmulttime.pdf. Did you forget to include PDF file with the graphs in it?\n")
    if not os.path.isfile("analysis.txt") and not os.path.isfile("analysis.pdf"):
        filesok=False        
        print("\nCANTFIND: analysis.txt (or pdf).\n")
    if filesok:
        print("\nSeems like you have all your files placed correctly!\n")

    unittest.main(exit=False)