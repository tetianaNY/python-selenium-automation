string = input('Input the string: ')
part = input('Input a replacement part of the string (the part have to be <= string and not empty): ')
replace = input('Input a new part to replace (the part have to be not empty): ')

if len(part) >= len(string) or part == '' or replace == '':
    print('Inputs does not match input conditions')
    quit()

def string_replacement(string, part, replace):
    string = string.upper()
    part = part.upper()
    i = 0
    for i in range(len(string)):
        if string[i:i+(len(part))] == part:
            string = string[:i] + replace + string[i+(len(part)):]

    return string

print(string_replacement(string, part, replace))

