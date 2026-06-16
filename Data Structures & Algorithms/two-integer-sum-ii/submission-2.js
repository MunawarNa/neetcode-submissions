class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {

        let left = 0;
        let right = numbers.length - 1

        while (left < right){
            let sumS = numbers[left] + numbers[right]

            if (sumS > target){
                right -= 1
            }
            else if (sumS < target){
                left += 1
            }
            else{
                return [left + 1, right + 1]
            }
        }
    }
}
