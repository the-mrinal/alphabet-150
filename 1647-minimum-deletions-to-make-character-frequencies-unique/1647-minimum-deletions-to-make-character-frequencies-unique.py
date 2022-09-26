'''

aab
a:2
b:1

aaabbbcc
a:3
c:1
d:2
e:0



'''


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        
        values = list(freq.values())
        
        values.sort()
#        1  2 2 3 3 
        visited = set() # 3 2 1
        
        count = 0
        
        for i in range(len(values) - 1,-1,-1):
            curr = values[i]
            while curr in visited and curr > 0:
                count += 1
                curr -= 1
            if curr != 0:
                visited.add(curr)
        
        return count
            