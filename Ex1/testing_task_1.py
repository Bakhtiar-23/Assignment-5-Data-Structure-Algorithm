import numpy as np
import time
import matplotlib.pyplot as plt

def print_element(matrix):
    return matrix[0][0]

# Testing the time complexity for different sizes of matrices
sizes = [10, 100, 1000, 5000, 10000]
times = []

for size in sizes:
    matrix = np.random.randint(1, 100, (size, size))
    start_time = time.time()
    print_element(matrix)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(sizes, times, marker='o')
plt.title('Task 1: Time Complexity of Printing Element at (0,0)')
plt.xlabel('Matrix Size (n x n)')
plt.ylabel('Time (seconds)')
plt.grid()
plt.show()
