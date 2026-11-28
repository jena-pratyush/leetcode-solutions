class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count =[0] * 26
        for letter in s:
            count[ord(letter) - ord('a')] += 1
        for letter in t:
            count[ord(letter) - ord('a')] -= 1
            
        return all(x == 0 for x in count)