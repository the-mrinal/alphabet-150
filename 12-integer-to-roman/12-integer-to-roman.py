class Solution:
    def intToRoman(self, num: int) -> str:
        intoRoman = [
            [1,'I'],
            [4,'IV'],
            [5,'V'],
            [9,'IX'],
            [10,'X'],
            [40,'XL'],
            [50,'L'],
            [90,'XC'],
            [100,'C'],
            [400,'CD'],
            [500,'D'],
            [900,'CM'],
            [1000,'M']
        ]
        
        ans = []
        for i in range(12,-1,-1):
            val,sym = intoRoman[i]
            q = num // val
            num = num % val
            ans.append(sym*q)
        return ''.join(ans)