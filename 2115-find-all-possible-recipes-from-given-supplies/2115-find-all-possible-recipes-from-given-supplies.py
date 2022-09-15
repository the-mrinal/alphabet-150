class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        curr_supplies = set(supplies)
        possible = [False]*n
        new_recipie = True
        
        while new_recipie:
            new_recipie = False
            
            for i in range(n):
                flag = True
                if not possible[i]:
                    for ing in ingredients[i]:
                        if ing not in curr_supplies:
                            flag = False
                            break
                    if flag:
                        possible[i] = flag
                        new_recipie = True
                        curr_supplies.add(recipes[i])
        
        result = []
        for i in range(n):
            if possible[i]:
                result.append(recipes[i])
        
        return result
                        