class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {

        let left = 0
        let right = heights.length - 1

        let maxWater = 0

        while (left < right){
            let h = Math.min(heights[left], heights[right])
            let w = right - left
            let area = h * w
            maxWater = Math.max(maxWater, area)

            if (heights[left] < heights[right]){
                left += 1
            }
            else{
                right -= 1
            }
        

        }
        return maxWater
    }
}
