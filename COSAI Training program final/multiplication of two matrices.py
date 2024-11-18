def multiply_matrices(matrix1, matrix2):
    """Multiply two matrices."""
    if len(matrix1[0]) != len(matrix2):
        return "Number of columns in matrix1 must be equal to number of rows in matrix2."
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_product = 0
            for k in range(len(matrix2)):
                sum_product += matrix1[i][k] * matrix2[k][j]
            row.append(sum_product)
        result.append(row)
    
    return result

# Example usage
if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    
    result = multiply_matrices(matrix1, matrix2)
    print("Product of matrices:")
    for row in result:
        print(row)
