import numpy as np
import time
import matplotlib.pyplot as plt

def double_first_row(matrix):
    matrix[0] = matrix[0] * 2
    return matrix

# Testing the time complexity for different sizes of matrices
sizes = [10, 100, 1000, 5000, 10000]
times = []

for size in sizes:
    matrix = np.random.randint(1, 100, (size, size))
    start_time = time.time()
    double_first_row(matrix)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(sizes, times, marker='o', color='orange')
plt.title('Task 2: Time Complexity of Doubling First Row')
plt.xlabel('Matrix Size (n x n)')
plt.ylabel('Time (seconds)')
plt.grid()
plt.show()
