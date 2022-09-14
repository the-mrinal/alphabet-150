class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dictionary = defaultdict(int)
        
        for num in arr:
            dictionary[num] += 1
        
        cache = set()
        
        for val in dictionary.values():
            if val in cache:
                return False
            cache.add(val)
        return True