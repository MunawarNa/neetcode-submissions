class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result +=  str(len(i))+ "#" + i
        return result
    """
    5#Hello5#World
    """
    def decode(self, s: str) -> List[str]:

        result = []

        j = 0
        i = 0
        while i < len(s):
            i = j
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            result.append(s[i:j])
            i = j
        return result
        
            


