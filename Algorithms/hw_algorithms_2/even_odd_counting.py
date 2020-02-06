

b = int(input('Enter the number: '))

def odd_even_counting(b):
    odd_counter = 0
    even_counter = 0
    while b > 0:
        if (b//10) % 2 == 0:
          even_counter = even_counter + 1
          b = b // 10
        else:
            odd_counter = odd_counter + 1
            b = b // 10
    return even_counter, odd_counter


print(odd_even_counting(b))
