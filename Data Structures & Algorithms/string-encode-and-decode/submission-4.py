class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ""
        for i in strs:
            encode += str(len(i)) + "#" + i
        
        return encode

    def decode(self, s: str) -> List[str]:

        i = 0
        j = 0
        result = []

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

