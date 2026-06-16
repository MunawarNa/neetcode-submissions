class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sort_s = sorted(list(s))
        sort_t = sorted(list(t))
        
        if len(sort_s) != len(sort_t):
             result = False

        elif len(sort_s) == len(sort_t):
            for i in range(len(sort_s)) :
                if  sort_s[i] != sort_t[i]:
                    result = False
                    break
                elif sort_s[i] == sort_t[i]:
                    result = True
        return result
            



        
