class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_count = {}

        for i in nums : 
            nums_count[i] = nums_count.get(i,0) + 1
        
        sorted_nums = dict(sorted(nums_count.items(), key=lambda item: item[1]))

        nums_list = list(sorted_nums)
        return nums_list[-k:]

        
