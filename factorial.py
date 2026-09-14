def factorial(n):
    result = 1
    if n == 0 or n == 1:
        return 1
    for i in range(n, 0, -1):
        result *= i
    return result

while True:
    try:  
        n = int(input('Enter your number '))
        if n < 0 :
            print('Error! factorial does not defined for negative numbers')
            continue
        print(f'The factorial of {n} is => {factorial(n)}')
    except:
        print('Error!')
        