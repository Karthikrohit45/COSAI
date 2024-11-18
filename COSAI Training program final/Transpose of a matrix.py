def transpose_matrix(matrix):
    """Transpose a matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    result = transpose_matrix(matrix)
    print("Transpose of matrix:")
    for row in result:
        print(row)
