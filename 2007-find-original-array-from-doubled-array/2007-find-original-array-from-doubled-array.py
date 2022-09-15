class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        freq = Counter(changed)
        res = []
        changed.sort(reverse = True)
        def isValid(num):
            if num == 0:
                if freq[num] >= 2:
                    freq[num] -= 1
                    return True  
            elif num % 2 == 0 and freq[num] > 0 and num // 2 in freq and freq[num // 2] >= 1:
                freq[num] -= 1
                return True
            return False

        for num in changed:
            if isValid(num):
                freq[num // 2] -= 1
                res.append(num // 2)

        return res if len(res) == n // 2 else []