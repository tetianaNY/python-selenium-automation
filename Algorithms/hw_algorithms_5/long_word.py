string = input('Input string: ')
def long_word(string):
    string_word = []
    string_word = string.split(' ')
    return f' The longest word is {sorted(string_word)[-1:]}'

print(long_word(string))