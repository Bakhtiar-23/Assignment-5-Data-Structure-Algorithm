import math

def calculate_time(n_initial, time_initial, n_target, complexity):
    
    if complexity == 'n^2':
        time_target = time_initial * (n_target ** 2) / (n_initial ** 2)
    elif complexity == 'log2':
        time_target = time_initial * (math.log2(n_target) / math.log2(n_initial))
    else:
        raise ValueError("Unsupported complexity function.")
    
    return time_target

# Initial conditions
n_initial = 1000
time_initial = 1  # in seconds
n_target = 10000

# Calculate time for n^2 complexity
time_n_squared = calculate_time(n_initial, time_initial, n_target, 'n^2')
print(f"Time to sort {n_target} items with O(n^2) complexity: {time_n_squared:.2f} seconds")

# Calculate time for log2 complexity
time_log2 = calculate_time(n_initial, time_initial, n_target, 'log2')
print(f"Time to sort {n_target} items with O(log2 n) complexity: {time_log2:.2f} seconds")
