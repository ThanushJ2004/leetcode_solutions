from typing import List

class Solution:
    def is_prime(self,n):
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False
        return True
    def closestPrimes(self, left: int, right: int) -> List[int]:
        a=0
        pa=0
        b=0
        n=right
        step=1
        if left>2:
            step=2
        if left!=2:
            if left%2==0:
                left+=1
        for i in range(left,right+1,step):
            if self.is_prime(i):
                if (i-b)<n:
                    a=b
                    b=i
                    pa=a
                    pb=b
                    n=b-a
                else:
                    a=b
                    b=i
        print(pa,pb)
        if pa==0:
            return [-1,-1]
        else:
            return [pa,pb]
a=Solution()
print(a.closestPrimes(1,100))