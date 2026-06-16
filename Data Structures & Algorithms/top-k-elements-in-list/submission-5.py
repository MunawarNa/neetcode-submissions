class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for i in nums:

            hashmap[i] = hashmap.get(i, 0) + 1

        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse = True))

        top_k_freq = list(sorted_hashmap)

        return top_k_freq[:k]
