import numpy as np
import time
import matplotlib.pyplot as plt

# Task 3: Function to double all elements of the entire matrix
def double_entire_matrix(matrix):
    return [[x * 2 for x in row] for row in matrix]

# Test the performance of doubling the entire matrix
matrix_sizes = [10, 100, 200, 500, 1000]
execution_times = []

for size in matrix_sizes:
    # Create a size x size matrix filled with random integers
    matrix = np.random.randint(1, 100, (size, size)).tolist()
    
    # Measure the execution time
    start_time = time.time()
    double_entire_matrix(matrix)
    end_time = time.time()
    
    execution_times.append(end_time - start_time)

# Plot the results
plt.plot(matrix_sizes, execution_times, label='Empirical Time Complexity')
plt.xlabel('Matrix Size (n x n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Empirical Time Complexity for Doubling Entire Matrix')
plt.legend()
plt.show()

# Add a pause to keep the window open
input("Press Enter to exit...")
