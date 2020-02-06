

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a > b and a > c:
    print(f'{a} is a biggest number')
elif b > a and b > c:
    print(f'{b} is a biggest number')
elif c > a and c > b:
    print(f'{c} is a biggest number')
else:
    print("We don't have a biggest number")


