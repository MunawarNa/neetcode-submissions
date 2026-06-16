class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {

        let left = 0;
        let right = height.length - 1;
        let leftMax = 0;
        let rightMax = 0;
        let trappingWater = 0

        while (left < right) {

            if (height[left] < height[right]){
                if (height[left] >= leftMax){
                    leftMax = height[left];
                }
                else{
                    trappingWater += leftMax - height[left];
                }
                left += 1
            }
            else{
                if (height[right] >= rightMax){
                    rightMax = height[right]
                }
                else{
                    trappingWater += rightMax - height[right]
                }
                right -= 1
            }
        }
        return trappingWater

    }
}
