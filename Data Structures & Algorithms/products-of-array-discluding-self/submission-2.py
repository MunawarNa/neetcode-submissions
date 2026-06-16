class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = len(nums) * [1]

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]
        
        return result
            


        