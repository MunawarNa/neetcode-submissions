class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {

        let start = 0;
        let maxFreq = 0;
        let maxLength = 0;
        let state = {};


        for (let end = 0; end < s.length ; end ++){

            state[s[end]] = (state[s[end]] || 0) + 1;
            maxFreq = Math.max(maxFreq, state[s[end]])

            if (k + maxFreq < end - start + 1){
                state[s[start]] -= 1;
                start += 1;
            }

            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength
        
    }
}
