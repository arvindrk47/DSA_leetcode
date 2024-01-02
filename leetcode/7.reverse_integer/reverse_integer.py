class Solution:
    def rev(self,x):
        temp =0
        while(x>0):
            ld = x%10
            temp = temp*10+ld
            x=x//10
        return temp
    
    def reverse(self, x: int) -> int:
        if x<0:
            x=x*-1
            x=self.rev(x)
            if x>=2**31-1:
                return 0
            return x*-1
        else:
            x=self.rev(x)
            if x>=2**31-1:
                return 0
            return x  
        