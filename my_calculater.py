
def my_sum(a, b):
    print(f'a + b = {a + b}')
def my_min(a, b):
    print(f'a - b = {a - b}')
def my_mul (a, b):
    print(f'a * b = {a * b}')
def my_div (a, b):
    print(f'a / b = {a / b}')

def my_calculater():

    a = int(input('please enter your number: \n'))
    b = int(input('please enter your second number: \n'))
    operation = (input('please entery your operations :\n'))

    if operation == '+':
        my_sum(a, b)
    elif operation == '-':
        my_min(a, b)
    elif operation == '*':
        my_mul(a, b)
    elif operation == '/':
        my_div(a, b)
    else:
        print('Not supported')

my_calculater()