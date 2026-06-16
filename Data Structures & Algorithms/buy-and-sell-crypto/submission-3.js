class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {

        let maxProfit = 0;
        let start = 0;
        let end = 0;

        while (end < prices.length){

            if (prices[start] < prices[end]){
                maxProfit = Math.max(maxProfit, prices[end] - prices[start]);
            }
            else {
                start = end
            }
            end += 1
        }
        return maxProfit
    
    }
}
