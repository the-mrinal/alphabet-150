'''
make a dict



'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phonePad = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z'],
        }
        
        n = len(digits)
        
        def createComb(index):
            if index == n:
                return []
            
            subAns = createComb(index + 1)
            
            new_ans = []
            
            for letter in phonePad[digits[index]]:
                for child in subAns:
                    new_ans.append(letter + child)
            return new_ans if new_ans else phonePad[digits[index]]
        
        return createComb(0)
                