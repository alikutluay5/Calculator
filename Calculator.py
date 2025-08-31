print('Hello, Enter Your Numbers')
input1 = input('Enter Your First Number: ')
input2 = input('Enter Your Second Number: ')
print('+ is Addition')
print('- is Substraction')
print('* is Multiplication')
print('/ is Division')
input3 = input('Select Your Operation (+, -, *, /): ')

if input3 == '+':
    result = float(input1) + float(input2)
    print('The Result is :', result)
    print('Thank you for using the calculator!')
elif input3 == '-':
    result = float(input1) - float(input2)
    print('The Result is :', result)
    print('Thank you for using the calculator!')
elif input3 == '*':
    result = float(input1) * float(input2)
    print('The Result is :', result)
    print('Thank you for using the calculator!')
elif input3 == '/':
    result = float(input1) / float(input2)
    print('The Result is :', result)
    print('Thank you for using the calculator!')
else:
    print('Invalid Operation Selected. Please try again.')
    exit()