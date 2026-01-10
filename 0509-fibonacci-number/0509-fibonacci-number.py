class Solution:
    def funct(self,num):
        if num ==0 or num==1:
            return num
        return self.funct(num-1)+self.funct(num-2)
    def fib(self, n: int) -> int:
        return self.funct(n)
