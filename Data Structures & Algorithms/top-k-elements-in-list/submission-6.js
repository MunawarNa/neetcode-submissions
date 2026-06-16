class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        const hashmap = {};

        for (let i of nums){

            hashmap[i] = (hashmap[i] || 0) + 1;
        }

        const sortedHashmap = Object.keys(hashmap).sort((a, b) => hashmap[b] - hashmap[a]);

        return sortedHashmap.slice(0, k).map(Number);
    }
}
