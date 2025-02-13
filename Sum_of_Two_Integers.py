class Solution(object):
    def getSum(self, a, b):
     
        
        while b != 0:
            tmp = (a & b)<<1
            a = a ^ b
            b = tmp
        return a
