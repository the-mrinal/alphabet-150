class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        
        words.sort(key=len)
        
        for w in words:
            dp[w] = max([dp[w[:i]+w[i+1:]] + 1 for i in range(len(w))])
        
        return max(dp.values())