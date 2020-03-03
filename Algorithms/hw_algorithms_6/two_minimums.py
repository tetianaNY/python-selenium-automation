

def two_min(array):
    new_array = []
    new_array.append(min(array))
    array.remove(min(array))
    new_array.append(min(array))
    return f' Minimum N1: {new_array[0]} Minimum N2: {new_array[1]}'

print(two_min([33, 44, 55, 66, 77, 34]))
