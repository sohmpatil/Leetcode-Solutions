class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def findPalin(s, start, end) :
            while(start >= 0 and end < len(s) and s[start] == s[end]) :
                start = start -1
                end = end + 1
            return s[start+1:end]

        for i in range(len(s)):
            
            s1 = findPalin(s, i, i)   # for odd
            s2 = findPalin(s, i, i+1) # for even
            
            if len(s1) > len(res) : res = s1
            if len(s2) > len(res) : res = s2
        
        return res