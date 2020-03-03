def max_of_min_string(matrix):
    a = 0
    temp_matrix = []
    for i in range(len(matrix)):
        temp_matrix.append(min(matrix[i]))
    print(temp_matrix)
    return f'Max of mins element: {max(temp_matrix)}'

print(max_of_min_string([[1,2,3], [4,5,6], [7,8,9]]))

print(max_of_min_string([[55,2,33], [14,15,6], [57,38,29]]))