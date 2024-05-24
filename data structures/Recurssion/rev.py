def rev(n,s=0):
    sum=0
    if n==0:
        return s
    else: 
        return rev(n//10, s*10+n%10)
    
n=12345
num=rev(n)
print(num)
