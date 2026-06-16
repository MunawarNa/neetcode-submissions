class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()

        start = 0
        longest_sub = 0

        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            longest_sub = max(longest_sub, end - start + 1)

        return longest_sub

        
        