class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {

        let charSet = new Set();

        let start = 0
        let longestSub = 0

        for (let end = 0; end < s.length; end++){
            while (charSet.has(s[end])){
                charSet.delete(s[start]);
                start += 1
            }
            
            charSet.add(s[end]);
            longestSub = Math.max(longestSub, end - start + 1)
            
        }
        return longestSub
    }

}
