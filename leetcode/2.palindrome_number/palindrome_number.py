class Solution:
    def isPalindrome(self, x: int) -> bool:
        number =x
        temp=0
        
        if x<0 or (x!=0 and x%10==0):
            return False
        while(x>0):
            ldigit=x%10
            temp =temp*10+ldigit
            x=x//10
        return number == temp