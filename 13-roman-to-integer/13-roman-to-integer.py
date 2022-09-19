class Solution:
    def romanToInt(self, s: str) -> int:
        currSum = 0
        n = len(s)
        val_map = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }
        
        i = 0
        while i < n:
            if (i < n - 1 and (s[i:i+2] in val_map)):
                currSum += val_map[s[i:i+2] ]
                i += 2
            else:
                currSum += val_map[s[i]]
                i += 1
        return currSum
                
                
                
                