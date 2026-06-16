class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_k = {}
        result = []
            
        for i in range(len(nums)):
            if nums[i] in frequent_k:
                frequent_k[nums[i]] = frequent_k[nums[i]] + 1
            else:
                frequent_k[nums[i]] = 1
        sorted_frequent_k = dict(sorted(frequent_k.items(), key = lambda x:x[1]))

        largest_num = 0
        for j in sorted_frequent_k :
            if sorted_frequent_k[j] >= largest_num:
                largest_num = sorted_frequent_k[j]
                result.append(j)
        return result[-k:]
        
