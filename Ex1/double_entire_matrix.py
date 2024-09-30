def double_entire_matrix(matrix):
    return [[x * 2 for x in row] for row in matrix]

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = double_entire_matrix(matrix)
    
    print("\nAfter doubling the entire matrix:")
    for row in matrix:
        print(row)
