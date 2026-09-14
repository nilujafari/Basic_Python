def average(scores):
    total = sum(scores)
    length = len(scores)
    average = total / length
    return average
student_count = int(input('How many student do you have?\n'))

for i in range(student_count):
    name = input('enter student Name:\n')
    scores = []
    for j in range(2):
        s = float(input('enter student Scores:\n'))
        scores.append(s)
    ave = average(scores)

    if ave >= 17:
        print(f'{name}, Averag score = {ave}, Exellent')
    elif ave <= 16:
        print(f'{name}, Averag score = {ave}, Good')
    else:
        print(f'{name}, Averag score = {ave}, Fail')