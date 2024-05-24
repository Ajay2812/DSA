def count_zeros(num,c):
    if num==0:
        return c
    if num%10==0:
        return count_zeros(num//10,c+1)
    return count_zeros(num//10,c)
    
n=100200308
c=0
ans=count_zeros(n,c)
print(ans)