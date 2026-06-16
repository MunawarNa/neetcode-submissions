class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {}
        for i in nums:

            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        
        sorted_dict = dict(sorted(nums_dict.items(), key= lambda item: item[1],  reverse=True))

        sorted_key_list = list(sorted_dict.keys())
        return sorted_key_list[:k]
