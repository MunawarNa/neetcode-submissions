class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict = {}

        for i in nums:

            if i in dict:
                dict[i] = dict[i] + 1
                return True
            else:
                dict[i] = 1

        return False