
def my_temperator():

    temperator = float(input('enter your temperator: \n'))
    temperator_type = input('pls enter your temperator type:[F, C]: \n').upper()

    if temperator_type == 'F':
        fahrenheit = (temperator * 9/5) + 32
        print(f'{fahrenheit} F')
    elif temperator_type == 'C':
        celsius = (temperator - 32)/1.8
        print(f'{celsius} C')
    else:
        print('wrong type')
my_temperator()