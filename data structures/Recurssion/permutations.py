#from itertools import permutations
#s="abc"
#perms=permutations(s)
##for perm in perms:
#    print(''.join(perm))


def permutations(p,up):
    if not up:
        print(p)
        return 
    ch=up[0]
    for i in range(len(p)):
        f=p[:i]
        s=[p[i:len(p)]]
        permutations(f+ch+s,up[1:])
permutations("","abc")
