import time
start = time.time()
class Solution:
    def lengthLongestSubstring(self, s):
        last_seen = {}
        left = 0
        sub_start = 0
        sub_length = 0
        for right,ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            current_length = right - left + 1
            if current_length > sub_length:
                sub_length = current_length
                sub_start = left
        best_substring = s[sub_start: sub_start+sub_length]
        return sub_length , best_substring
solve = Solution()
length, substring = solve.lengthLongestSubstring("abcabcbb")
print("length:" ,length)
print("substring:", substring)

end = time.time()
print(end -start)
