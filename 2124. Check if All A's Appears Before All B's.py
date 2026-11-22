class Solution(object):
    def checkString(self, s):
        for i in range (0, len(s)-1):
            if s[i] == "b":
                if s[i+1] == "a":
                    return False
                    break
        else:
            return True
            
        