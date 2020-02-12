

def devision(num1, num2, accur):

# считаем целые или возвращаем 0

    count = 0
    result = ''
    while num1 >= num2:
        num1 = num1 - num2
        count += 1
    if num1 == 0:
        result = str(count)
        result += '.0'
        return result
    i = 0
    float_result = []
    num1_2 = num1

# сколько знаков после запятой
    for i in range(accur):
      float_index = 0
      count2 = 0

# умножаем на 10 для вычитания
      while num1_2 <= num2:
          num1_2 *= 10
          float_index += 1
          if num1_2 == 0: break

# добавляем 0, после запятой, если нет возможности поделить на цело
      q = 1
      if float_index > 1:
        for q in range(float_index-1):
          float_result.append('0')

      print(i)


# вычитаем и записываем в список количество вычитаний на этом десятке
      while num1_2 >= num2:
          num1_2 = num1_2 - num2
          count2 += 1
      # print(count2)
      float_result.append(str(count2))

    print(float_result)
    result = str(count)
    result += '.'
    result += ''.join(float_result)

    return result

print("The total is", devision(1, 1777, 100))

