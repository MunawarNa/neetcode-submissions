class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {

        const numSet =  new Set(nums);

        let longest = 0;

        for (let num of numSet){

            if (!numSet.has(num - 1)) {
                let current = num;
                let currentStreak = 1;

                while (numSet.has(current + 1)){
                    current += 1
                    currentStreak += 1
                }
                longest = Math.max(longest, currentStreak)
            }
        }
        return longest
    }
}
