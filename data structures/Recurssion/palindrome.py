import math
def helper(n,digits):
    if n%10==n:
        return n
    else:
        rem=n%10
        return rem*int(math.pow(10,digits-1))+ helper(n//10,digits-1)
    
def rev(n):
    return n==helper(n,int(math.log10(n)+1))

n=123421
print(rev(n))

