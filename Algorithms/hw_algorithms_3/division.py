
# деление num1 на num2 с точностью accur

def devision(num1, num2, accur):

# считаем целые или возвращаем 0

    count = 0
    result = ''
    while num1 >= num2:
        num1 = num1 - num2
        count += 1
    if num1 == 0:
        result = str(count)
        result += '.00'
        return result
    i = 0
    float_result = []
    num1_2 = num1
    count_0 = 0

# сколько знаков после запятой
    for i in range(accur):
      float_index = 0
      count2 = 0
      if num1_2 == 0: break

# Так как у нас десятичная система счисления, умножаем на 10 для вычитания. Каждая 10 это 1 разряд.
      while num1_2 <= num2:
          num1_2 *= 10
          float_index += 1
          # print(float_index)
          if num1_2 == 0: break

# добавляем 0, после запятой, если нет возможности поделить нАцело. (Вычесть с положительным остатком)
      q = 1
      if float_index > 1:
        for q in range(float_index-1):
          float_result.append('0')
          count_0 += 1



# вычитаем и записываем в список количество вычитаний на этом десятке, также как в начале получали целое число
      # только для каждого разряда после запятой

      while num1_2 >= num2:
          num1_2 = num1_2 - num2
          count2 += 1
      float_result.append(str(count2))

    result = str(count)
    result += '.'
    result += ''.join(float_result)

    return result[:len(result)-count_0]

print("The total is", devision(1, 177, 100))

