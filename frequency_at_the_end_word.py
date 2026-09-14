with open("sample.txt", 'r') as f:
    data = f.read().lower().split()
    puct = ",./!?:'\|"
    freq = {}
for ch in data:
    clear_ch = ch.strip(puct)
    if clear_ch == "" :
        continue
    last_ch = clear_ch[-1]
    if last_ch.isalpha():
        if last_ch in freq:
            freq[last_ch] += 1
        else:
            freq[last_ch] = 1

sort_last_w = sorted(freq.items(), key=lambda x : x[0])
print(sort_last_w)






"""" Test """
#    if len(ch) > 2:
#         secound_freq = ch[-2]
#         if secound_freq.isalpha():
#             if secound_freq in freq_secound:
#                 freq_secound[secound_freq] += 1
#             else:
#                 freq_secound[secound_freq] = 1
# print( freq_secound)