class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}

        for i in range(len(strs)):
            sorted_i = sorted(strs[i])
            sorted_i = "".join(sorted_i)
            if sorted_i in dict:
                dict[sorted_i].append(strs[i])
            else:
                dict[sorted_i] = [strs[i]]
        return [*dict.values()]