class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}

        for i in nums:
            if i in my_dict:
                my_dict[i] = my_dict[i] + 1
            else:
                my_dict[i] = 1
        
        sorted_items = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

        top_k = list(sorted_items)

        return top_k[:k]