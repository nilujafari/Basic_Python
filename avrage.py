def my_average(numbers):
    total = sum(numbers)
    length  = len(numbers)
    average = total / length
    return average

list_of_numbers = [2,7,4,9]
result = my_average(list_of_numbers)
print(f'your average is = {result}')