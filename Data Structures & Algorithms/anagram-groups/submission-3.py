class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}

        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in map:
                map[sorted_i].append(i)
            else:
                map[sorted_i] = [i]
        return [*map.values()]
