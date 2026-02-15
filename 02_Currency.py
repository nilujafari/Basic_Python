info = {
    "USD": {
        "EURO":1/1.1,
        "GBP":1/1.20
    },
    "EURO": {
        "USD": 1.1,
        "GBP": 0.9
    },
    "GBP": {
        "USD": 1.20,
        "EURO": 1.25
    }
}
while True:
    try:
        value = int(input('please enter your value: '))
    except:
        print('Error! please try again')
        continue
    
    print('Select (input) currency from the list: ')
    for item in info.keys():
        print(f"{item}")
    input_currency = input('Please enter your choice: ').upper()

    if input_currency not in info.keys():
        print("Currency not available! Please try again")
        continue

    print('Select (output) currency from the list: ')
    for item in info.keys():
        print(f"{item}")
    output_currency = input('Please enter your choice: ').upper()
    
    if output_currency not in info.keys():
        print("Currency not available! Please try again")
        continue

    result = value * info[input_currency][output_currency]
    print(f'{result} {output_currency}')
    