class Solution:
    def removePalindromeSub(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        
        isPalin = True
        
        while i < j:
            if s[i] != s[j]:
                isPalin = False
            i += 1
            j -= 1
        if isPalin:
            return 1
        return 2