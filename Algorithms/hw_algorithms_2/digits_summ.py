# Считает сумму любых введеных целых чисел

b = int(input('Enter the number: '))

def digits_summ(b):
    summ_string = 0
    while b > 0:
        summ_string = summ_string + (b % 10)
        b = b // 10
    return summ_string
print(digits_summ(b))

