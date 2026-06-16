class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for i in matrix:
            nums += i
        print(nums)

        left = 0
        right = len(nums) - 1

        while left <= right : 
            mid = (left + right) // 2
            if nums[mid] == target :
                return True
            
            if nums[mid] > target :
                right = mid - 1
            else:
                left = mid + 1
        return False