class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        A_len = len(start)
        B_len = len(end)
        
        if A_len != B_len:
            return False
        
        if start.replace('X','') != end.replace('X',''):
            return False
        
        i,j = 0,0
        
        while i < A_len and j < B_len:
            
            while i < A_len and start[i] == 'X':
                i += 1
            
            while j < B_len and end[j] == 'X':
                j += 1
            
            if i == A_len and j == B_len:
                return True
            if i == A_len or j == B_len:
                return False
            
            if start[i] != end[j]:
                return False
            
            if start[i] == 'L' and j > i:
                return False
            if start[i] == 'R' and i > j:
                return False
            
            i += 1
            j += 1
        
        return True