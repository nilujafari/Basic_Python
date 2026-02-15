def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

while True:
    try:  
        n = int(input('Enter your number '))
        if n < 0 :
            print('Error! factorial does not defined for negative numbers')
            continue
        print(f'The factorial of {n} is => {factorial_recursive(n)}')
    except:
        print('Error!')
        