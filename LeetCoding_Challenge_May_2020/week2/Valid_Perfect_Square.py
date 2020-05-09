class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num**(1/2)
        y=int(x)
        
        return x==y
