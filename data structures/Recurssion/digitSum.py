def digitSum(n):
    if n%10==n:
        return n
    return n%10+digitSum(n//10)




def pro(n):
    if n%10==n:
        return n
    return n%10 * pro(n//10)

print(pro(12345))
