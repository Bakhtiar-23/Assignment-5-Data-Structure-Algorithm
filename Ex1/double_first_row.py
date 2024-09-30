def double_first_row(matrix):
    if matrix and matrix[0]:
        matrix[0] = [x * 2 for x in matrix[0]]
    return matrix

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = double_first_row(matrix)
    
    print("\nAfter doubling the first row:")
    for row in matrix:
        print(row)
