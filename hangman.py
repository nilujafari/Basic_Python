import random
names = ["Hasan", "Ali", "Behnam", "Mohamad", "Vahid", "Amin", "Maryam", "zahra"]
select_name = random.choice(names).lower()
guess_count = len(select_name)
guess_list= ['-'] * len(select_name)
current_guess = " ".join(guess_list)
print(current_guess)
while guess_count >0 :
    guess_char = input("Enter your char:\n")
    if guess_char.isalpha():
        if guess_char in select_name :
            if guess_char in guess_list :
                print('you have guessed before, try new guess')
            else:
                for idx, char in enumerate(select_name):
                    if char == guess_char:
                        guess_list[idx] = guess_char
                current_guess = " ".join(guess_list)
                print(f'prfect => {current_guess}')

                if not '_' in guess_list:
                    print('you win!!!!')
                    break
        else:   
            guess_count -=1
            print(f'wrong! => remaind guess count {guess_count}')
    else:
        print("Enter a valid char")