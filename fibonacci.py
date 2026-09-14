def fibonacci(n):
    if n == 0:    
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

while True:
    try:  
        n = int(input('Enter your number '))
        if n < 0 :
            print('Error! fibonacci does not defined for negative numbers')
            continue
        print(f'The fibonacci of {n} is => {fibonacci(n)}')
    except:
        print('Error!')
        