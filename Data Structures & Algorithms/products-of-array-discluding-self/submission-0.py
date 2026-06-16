class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * (len(nums))
        postfix = [1] * (len(nums))
        result = []

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range((len(nums)-2),-1,-1):
            postfix[j] = postfix[j+1] * nums[j+1]
        for num in range(len(nums)):
            product = prefix[num] * postfix[num]
            result.append(product)
        return result

        