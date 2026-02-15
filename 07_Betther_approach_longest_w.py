sentence = 'Every day is a new chance to get betterr'
words = sentence.split()

word_lengths = {
    w: len(w) for w in words
}
sort_word = sorted(word_lengths.items(), key=lambda x:x[1], reverse= True)
print(sort_word)

def my_func(item):
    return item[1]
lambda_func = lambda item: item[1]

sort_word_lengths = sorted(word_lengths.items(), key=lambda x:x[1], reverse= True)
print(sort_word_lengths[0])

for idx,item in enumerate(sort_word_lengths):
    print(f"the {idx} longest word is : {item[0]} with length {item[1]}")
    