# работает только с текущим примером, может работать с любым примером в формате x0y0z0 ... n0 где xyzn буквы,
# 0 - одно разрядное число
# Завтра подумаю еще.
#
# Проблема в выделение числа из строки: можно выделить 1 разрядное,
# еще одним вложенным циклом еще один разряд и сколько циклов делать?

def decompression(comp_string):
    i = 0
    decom_list = []
    decom_string = comp_string[::2]
    # print(decom_string)
    for i in range(len(comp_string)):
        if comp_string[i] not in decom_string:
            # print(comp_string[i])
            decom_list.append(int(comp_string[i]))

    new_string = ''
    for i in range(len(comp_string)//2):
        new_string += decom_string[i] * decom_list[i]

    return new_string + comp_string[-1]



print(decompression('а4б3в2г'))