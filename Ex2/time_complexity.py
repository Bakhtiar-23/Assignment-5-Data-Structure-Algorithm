import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def T1(n):
    return 2 * n**2 - 3 * n + 2  # Quadratic

def T2(n):
    return 3 * n - 7  # Linear

def T3(n):
    return 2**n - 1  # Exponential

def T4(n):
    return 2 * n + 2 * n * np.log(n)  # Linearithmic

def T5(n):
    return 2 * n**2 + 2 * n * np.log(n)  # Quadratic

def T6(n):
    return 0.28 * n + 256  # Linear

# Generate values for n
n_values = np.arange(1, 21)  # From 1 to 20

# Calculate the function values
T1_values = T1(n_values)
T2_values = T2(n_values)
T3_values = T3(n_values)
T4_values = T4(n_values)
T5_values = T5(n_values)
T6_values = T6(n_values)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, T1_values, label='T(n) = 2n² - 3n + 2', marker='o')
plt.plot(n_values, T2_values, label='T(n) = 3n - 7', marker='o')
plt.plot(n_values, T3_values, label='T(n) = 2ⁿ - 1', marker='o')
plt.plot(n_values, T4_values, label='T(n) = 2n + 2n log(n)', marker='o')
plt.plot(n_values, T5_values, label='T(n) = 2n² + 2n log(n)', marker='o')
plt.plot(n_values, T6_values, label='T(n) = 0.28n + 256', marker='o')

# Add title and labels
plt.title('Time Complexity Functions')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.yscale('log')  # Use logarithmic scale for better visibility
plt.legend()
plt.grid()
plt.show()
