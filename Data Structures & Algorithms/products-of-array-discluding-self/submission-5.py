class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        result = []
        for i in range(len(nums)):
            temp_calc = 1
            for j in range(len(nums)):
                if j != i :
                    temp_calc *=  nums[j]
            result.append(temp_calc)
        
        return result