class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        newStartWords = set()
        for word in startWords:
            newStartWords.add("".join(sorted(word)))
        
        count = 0
        for target in targetWords:
            sortedT = "".join(sorted(target))
            for i in range(len(target)):
                if sortedT[:i] + sortedT[i+1:] in newStartWords:
                    count += 1
                    break
        
        return count