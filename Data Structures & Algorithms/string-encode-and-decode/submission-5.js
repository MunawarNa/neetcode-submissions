class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let string = ""
        for (let str of strs){
            string += str.length + "#" + str;
        }
        return string;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {

        let i = 0;
        
        let result = [];

        while (i < str.length){

           let j = i;

            while (str[j] !== "#"){

                j += 1;
            }

            let length = parseInt(str.slice(i, j))

            i = j + 1
            j = i + length
            result.push(str.slice(i, j))
            i = j
        }
        return result
    }
}
