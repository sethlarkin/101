'''
assign2.py
CMPS101 winter2016

Shaun Musikanth (smusikan@ucsc.edu)
and
Seth Larkin (sslarkin@ucsc.edu)

'''

from math import floor
import numpy as np
import timeit as ti
import matplotlib.pyplot as plt


# Problem 1: matmult(A,x). Multiply a matrix with a vector.
def matmult(A, x):
    n = A.shape[0]
    C = np.zeros(n, dtype=int)

    for i in range(n):
        for j in range(n):
            C[i] += A[i, j] * x[j]

    return C

# Problem 2: hadmat(k). Create hadamard of size 2^k.
def hadmat(k):
    if k == 0:
        return np.array([[1]])

    tile = hadmat(k - 1)
    A = np.concatenate([tile, tile])
    B = np.concatenate([tile, -tile])

    return np.concatenate([A, B], 1)

# Problem 4: hadmatmult(H,x). Takes hadamard H and vector x, multiplies.
def hadmatmult(H, x):
    # Base Case: ([a + b], [a - b])
    if len(x) == 2:
        C = np.zeros(2, dtype=int)

        a = H[0][0] * x[0]
        b = H[0][0] * x[1]

        C[0] = a + b
        C[1] = a - b

        return C

    x1 = x[:floor(len(x) / 2)]
    x2 = x[floor(len(x) / 2):]

    # Quadrant
    Q = H[:floor(len(H) / 2), :floor(len(H) / 2)]

    # Calculate both halves of the matrix and vector
    b11 = hadmatmult(Q, x1)
    b12 = hadmatmult(Q, x2)

    # Add the resulting vectors back together
    q1 = b11 + b12
    q2 = b11 - b12

    return np.concatenate([q1, q2])


if __name__ == '__main__':
    # Problem 5
    # Set input range and count
    input_range = range(1, 13)
    input_count = len(input_range)
    plot_range = [2 ** k for k in input_range]

    # Initialize execution time arrays
    matmult_exec_time = np.zeros(input_count)
    hadmatmult_exec_time = np.zeros(input_count)

    # Create timeit objects
    ti_matmult = ti.Timer(lambda: matmult(H, x))
    ti_hadmatmult = ti.Timer(lambda: hadmatmult(H, x))

    # Iterate through specified input range
    for k in input_range:
        print(k, "/", input_count)

        # Create hadamard matrix and random vector inputs
        H = hadmat(k)
        x = np.random.randint(-5, 50, 2 ** k)

        # Store execution times
        matmult_exec_time[k - 1] = ti_matmult.timeit(number=1)
        hadmatmult_exec_time[k - 1] = ti_hadmatmult.timeit(number=1)

    # Create pyplot matmult and hadmatmult figure
    plt.figure()

    plt.title("Matrix Multiplication Algorithms", fontsize=20)
    plt.xlabel("Input Size", fontsize=16)
    plt.ylabel("Time (seconds)", fontsize=16)

    plt.plot(plot_range, matmult_exec_time, 'r', label="Brute-force (matmult)", linewidth=2)
    plt.plot(plot_range, hadmatmult_exec_time, 'g', label="Divide and Conquer (hadmatmult)", linewidth=2)
    plt.legend()

    # Show plot
    plt.show()
