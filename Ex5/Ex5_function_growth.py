import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f1(n): return np.full(n.shape, 50)  # Return an array of 50s with the same shape as n
def f2(n): return np.log10(n)
def f3(n): return np.log2(n)
def f4(n): return np.sqrt(n)
def f5(n): return 100 * n
def f6(n): return n**2
def f7(n): return 2**n

# Generate a range of values for n
n = np.linspace(1, 20, 400)

# Calculate the function values
y1 = f1(n)
y2 = f2(n)
y3 = f3(n)
y4 = f4(n)
y5 = f5(n)
y6 = f6(n)
y7 = f7(n)

# Plotting the functions
plt.figure(figsize=(12, 8))

plt.plot(n, y1, label='50', color='red')
plt.plot(n, y2, label='log10(n)', color='blue')
plt.plot(n, y3, label='log2(n)', color='green')
plt.plot(n, y4, label='n^0.5', color='orange')
plt.plot(n, y5, label='100n', color='purple')
plt.plot(n, y6, label='n^2', color='brown')
plt.plot(n, y7, label='2^n', color='black')

plt.ylim(-10, 300)  # Set limits for y-axis for better visibility
plt.xlim(1, 20)  # Set limits for x-axis
plt.xlabel('n')
plt.ylabel('Function Value')
plt.title('Growth of Functions')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.legend()
plt.grid()
plt.show()
