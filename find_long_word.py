sentence = 'Every day is a new chance to get betterr'
data = sentence.split()
longest_word = ''
second_longest_word = ''
third_longest_word = ''
for idx, w in enumerate (data):
    if len(w) > len(longest_word):
        if len(longest_word) > len(second_longest_word):
            second_longest_word = longest_word
        longest_word = w
    elif len(w) > len(second_longest_word):
        second_longest_word = longest_word
        if len(second_longest_word) > len(third_longest_word):
            third_longest_word = second_longest_word
        longest_word = w
    elif len(w) > len(third_longest_word):
        third_longest_word = w
    print(f'{idx} : {w} => long_word: {longest_word}, second_longest: {second_longest_word}, third_longest: {third_longest_word} ')
print(longest_word, second_longest_word, third_longest_word)
