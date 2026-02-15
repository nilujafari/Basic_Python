"""this method is better than another method ... and this method better for real text.
  (punct = punctuation => (alaem negareshi)"""

with open("sample.txt", 'r') as file:
    data = file.read()
    list_of_words = data.split()
    punct = ".,?:'_ "
    count = 0
    for w in list_of_words :
        clean = w.strip(punct)
        if clean == "" :
            continue
        count += 1
    print(count)


# Second Method
with open("sample.txt", 'r') as file:
    data = file.read()
    list_of_words = data.split()
    exclusion = ['.', '-', '?', ',', '!', '"', ":"]
    word_count = 0
    for w in list_of_words:
        if w in exclusion:
            continue
        word_count += 1
    print(word_count , list_of_words)
