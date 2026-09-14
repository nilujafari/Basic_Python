def sum(a, b):
    result = (a + b)
    print(f'{a} + {b} = {result}')
def min(a, b):
    result = (a - b)
    print(f'a - b = {result}')
def mult(a, b):
    result = (a * b)
    print(f'a * b = {result}')
def div(a, b):
    result = (a / b)
    print(f'a / b = {result}')

def my_calculater():
    a = int(input('enter your first number:\n'))
    b = int(input('enter your secound number:\n'))
    operator = input('entery your option')

    if operator == '+':
        sum(a, b)
    elif operator == '-':
        min(a ,b)
    elif operator == '*':
        mult(a ,b)
    elif operator == '/':
        div(a,b)
    else:
        print('you are not corect operation or number\n')

my_calculater()