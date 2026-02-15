""" best basic method : dic counting """

with open("war-and-peace.txt", 'r') as f:
    data = f.read().upper()
    freq = {}
    for ch in data:
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
sort_freq = sorted(freq.items(), key=lambda x:x [1], reverse= True)
print(sort_freq)
