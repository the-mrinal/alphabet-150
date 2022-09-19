class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set(arr)
        freq = Counter(arr)
        for i in range(len(arr)):
            if arr[i] == 0:
                if freq[arr[i]] > 1:
                    return True
            elif 2*arr[i] in arr_set:
                return True
        return False