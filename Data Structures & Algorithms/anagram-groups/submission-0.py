class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        object_group = {}

        for i in range(len(strs)) :
            chars_sort = sorted(strs[i])
            sorted_strs = "".join(chars_sort)
            
            if sorted_strs in object_group:
                object_group[sorted_strs].append(strs[i])
            else:
                object_group[sorted_strs] = [strs[i]]

        return [*object_group.values()]
