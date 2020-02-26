# Уточняющие вопросы - В каком формате выводить? будут ли в строке равные по размеру самому большому?
# Самый простой код выглядит так, можно еще поставить цикл проверяющий длину каждого слова с самым большим и вывести его тоже.

string = input('Input string: ')
def long_word(string):
    string_word = []
    string_word = string.split(' ')
    return f' The longest word is {sorted(string_word)[-1:]}'

print(long_word(string))