import math
import pandas as pd

def performance_time(n):
    return {
        'log_2 n': math.log2(n),
        '√n': math.sqrt(n),
        'n': n,
        'n^2': n ** 2,
        'n!': math.factorial(n) if n <= 20 else float('inf')  
    }

input_sizes = [10, 1000, 10000, 100000]

results = {n: performance_time(n) for n in input_sizes}

df = pd.DataFrame(results).T

df = df * 1e6  

df = df.replace([float('inf')], 'Overflow')  

print(df)
