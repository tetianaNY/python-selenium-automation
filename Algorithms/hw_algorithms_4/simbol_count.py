a = input('Input string: ')
b = input('Input symbol: ')

def simbol_count(a, b):
    count = 0
    for symbol in a:
        if symbol == b:
            count += 1
    return count

print(simbol_count(a,b))