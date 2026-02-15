import time
start = time.time()
class Solution:
    def lengthLongestSubstring(self, text):
        active_chars = set()
        left_idx = 0
        max_length = 0
        for right_idx in range(len(text)):
            while text[right_idx] in active_chars:
                active_chars.remove(text[left_idx])
                left_idx += 1

            active_chars.add(text[right_idx])
            max_length = max(max_length, right_idx - left_idx + 1)
        return max_length    
solve = Solution()
resul = solve.lengthLongestSubstring("abcabcbb")
print(resul)
end = time.time()
print(end - start)
