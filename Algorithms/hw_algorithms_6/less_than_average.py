
def less_than_average(array):
    new_array = []
    x = sum(array)/len(array)
    for a in array:
        if a < x:
            new_array.append(a)
    return new_array



print(less_than_average([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11]))
print(less_than_average([154, 23, 375, 41, 5, 56, 273, 38, 90, 150, 11]))
