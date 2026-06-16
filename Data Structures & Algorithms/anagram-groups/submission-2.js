class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        const hashmap = {};

        for (let i = 0; i < strs.length; i++){

            let sortedStr = strs[i].split("").sort().join("");

            if (hashmap[sortedStr]){
                hashmap[sortedStr].push(strs[i]);
            }
            else {
                hashmap[sortedStr] = [strs[i]];
            }
        }
        return Object.values(hashmap);
        
    }
}
