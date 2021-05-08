
next = 'y'
while next == 'y':
    a = float(input('Type the first number: '))
    operation = input('Type the operation: ')
    b = float(input('The the second number: '))
    if operation == '+':
        print(a + b)

    elif operation == '-':
        print(a - b)

    elif operation == '*':
        print(a * b)

    elif operation == '/':
        print(a / b)

    else:
        print('Sorry you written incorrect symbol!')
    
    next = input('Do you want to continue? \n Type "y" to continue counting! If you want to finish the process type "enter" or any other key: ')