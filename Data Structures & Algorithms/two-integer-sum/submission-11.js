class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        let my_dict = {};

        for (let i = 0; i < nums.length; i++){

            let diff = target - nums[i];
            
            if (diff in my_dict){
                return [my_dict[diff], i];
            }

            else{
                my_dict[nums[i]] = i
            }
        }
    }
}
