def max_of_min_columns(matrix):
    a = 0
    temp_matrix = []
    for i in range(len(matrix)):
        temp_matrix1 = []
        for y in range(len(matrix[0])):
            temp_matrix1.append(matrix[y][i])
        temp_matrix.append(min(temp_matrix1))
    return f'Max of mins element: {max(temp_matrix)}'

print(max_of_min_columns([[1,2,3], [4,5,6], [7,8,9]]))

print(max_of_min_columns([[55,2,33], [14,15,6], [57,38,29]]))