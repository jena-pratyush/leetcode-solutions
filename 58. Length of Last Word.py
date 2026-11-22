class Solution(object):
    def lengthOfLastWord(self, s):
        last_word = 0
        for i in range (0, len(s)):

            if s[i] == " ":
                if i + 1 < len(s) and s[i+1] != " ":
                    last_word = 0
            
            else:
                last_word += 1

        return last_word