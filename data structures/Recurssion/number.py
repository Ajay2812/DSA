def print_num(n):
    if n==0:
        return
    else:
        print_num(n-1)
        print(n)
def fun_rev(n):
    if n==0:
        return
    print(n)
    fun_rev(n-1)

def fun_both(n):
    if n==0:
        return
    print(n)
    fun_both(n-1)
    print(n)

fun_both(5)
