import re
class Solution:

    def isPalindrome(self, s: str) -> bool:

        string = re.sub(r'[^a-zA-Z0-9]', "", s)
        

        i = 0
        j = len(string) -  1

        while i < j :

            if string[i].lower() != string[j].lower():
                return False
        
            i += 1
            j -= 1

        return True


        