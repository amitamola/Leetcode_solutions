// https://leetcode.com/problems/count-and-say/description/

class Solution:
    def sayer(self, string):
        crr = string[0]
        counter = 1
        final_str = ''
        
        for val in string[1:]:
            if val==crr:
                counter+=1
                
            else:
                final_str = final_str + str(counter)+str(crr)
                crr=val
                counter=1
                
        final_str = final_str + str(counter)+str(crr)
        return final_str


    def countAndSay(self, n: int) -> str:
        string_val = '1'

        if n==1:
            return string_val

        for _ in range(n-1):
            string_val = self.sayer(string_val)
        
        return string_val
