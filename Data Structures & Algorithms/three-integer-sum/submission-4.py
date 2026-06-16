class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i, a in enumerate(nums):

            if a>0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            k = i+1
            j = len(nums)-1

            while k < j:
                current_sum = a + nums[k] + nums[j]
                if current_sum < 0:
                    k +=1
                elif current_sum > 0:
                    j -=1
                else:
                    res.append([nums[i],nums[k],nums[j]])
                    k +=1
                    j -=1
                    while nums[k] == nums[k-1] and k<j:
                        k +=1
        return res

                

