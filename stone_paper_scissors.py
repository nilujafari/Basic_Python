import random

options = ['st', 'pa', 'sc']
user_score = 0
pc_score = 0
run = True

while run :
    print('st:stone', 'pa:paper', 'sc:scissors')
    user_choice = input('Please enter your choice: \n')
    if user_choice in options :
        pc_choice = random.choice(options)
        print(f'pc choice is: {pc_choice}')
        if user_choice == pc_choice:
            print('Equal')
        elif user_choice == 'st':
            if pc_choice == 'pa':
                pc_score += 1
            else:
                user_score += 1
        elif user_choice == 'pa':
            if pc_choice =='sc':
                pc_score += 1
            else:
                user_score += 1
        elif user_choice == 'sc':
            if pc_choice == 'st':
                pc_score += 1
            else:
                user_score += 1
        if user_score == 3 or pc_score == 3:
            if user_score == 3:
                print('YOU WIN!')
            else:
                print('Sorry, pc win')
            break
        else:
            print(f'user score : {user_score}    pc score : {pc_score}')
    else:
        print('ERROR! choice not true')
    