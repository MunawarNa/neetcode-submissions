class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left =  0
        right = len(numbers) - 1

        while left < right:
            sums = numbers[left] + numbers[right]

            if target == sums:
                return [left + 1, right + 1]
            elif target > sums:
                left += 1
            elif target < sums:
                right -= 1

        

        


