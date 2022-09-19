class UnionFind:
    
    def __init__(self,length):
        self.root = [i for i in range(length)]
        self.rank = [1 for i in range(length)]
    
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
    
        

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for a,b in pairs:
            uf.union(a,b)
        
        str_map = defaultdict(list)
        
        for i in range(n):
            parent_idx = uf.find(i)
            str_map[parent_idx].append([s[i],i])
        
        
        new_s = list(s)
        for key,val in str_map.items():
            temp = sorted(val)
            
            for i in range(len(val)):
                new_s[val[i][1]] = temp[i][0]
        
        return "".join(new_s)