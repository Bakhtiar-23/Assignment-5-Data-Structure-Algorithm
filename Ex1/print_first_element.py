def print_first_element(matrix):
    if matrix and matrix[0]:
        print(f"Element at (0,0): {matrix[0][0]}")
    else:
        print("Matrix is empty or not valid.")

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_first_element(matrix)
