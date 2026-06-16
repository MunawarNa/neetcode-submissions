class Solution:
    result = []
    original_str = []

    def encode(self, strs: List[str]) -> str:
        string = ''
        original_str = strs
        for i in strs:
            string = string + str(len(i)) + '#' + i
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result

  
  




