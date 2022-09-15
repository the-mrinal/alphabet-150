class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def minimizeW(A):
            prev = None
            count = 0
            new_s = []
            
            for w in A:
                if prev and prev == w:
                    count += 1
                elif prev:
                    count += 1
                    new_s.append(prev)
                    new_s.append(str(count))
                    prev = w
                    count = 0
                else:
                    prev = w
            if prev:
                count += 1
                new_s.append(prev)
                new_s.append(str(count))
            return ''.join(new_s)
        
        minS = minimizeW(s)
        minS_len = len(minS)
        count = 0
        for word in words:
            minW = minimizeW(word)
            
            if len(minW) == minS_len:
                flag = True
                for i in range(1,minS_len,2):
                    if minW[i] > minS[i]:
                        flag = False
                        break
                    if minW[i - 1] != minS[i - 1]:
                        flag = False
                        break
                    if minS[i] < '3' and minW[i] < minS[i]:
                        flag = False
                        break
                if flag:
                    count += 1
        return count