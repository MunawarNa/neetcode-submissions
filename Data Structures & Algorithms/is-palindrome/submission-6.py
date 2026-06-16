class Solution:
    def isPalindrome(self, s: str) -> bool:

        s.split(" ")
        alphanum = ""
        for i in s:
            if i.isalnum():
                alphanum += i.lower()
        
        i = 0
        j = len(alphanum) - 1

        while i < j:
            if alphanum[i] != alphanum[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
