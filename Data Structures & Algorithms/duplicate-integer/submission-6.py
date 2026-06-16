class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_list = []

        for i in nums:

            if i in nums_list:
                return True
            else:
                nums_list.append(i)
        return False
