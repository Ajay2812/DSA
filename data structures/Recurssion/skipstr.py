def skip(up):
    if not up:
        return ""
    ch=up[0]
    if ch=='a':
        return skip(up[1:])
    else:
        return ch+skip(up[1:])
    
def skip(p,up):
    if not up:
        return p
    ch=up[0]
    if ch=='a':
        return skip(p,up[1:])
    else:
        return skip(p+ch,up[1:])
    
def skipapple(up):
    if not up:
        return ""
    if up.startswith("apple"):
        return skipapple(up[5:])
    else:
        return up[0]+skipapple(up[1:])
    

up="bdapplehhappleba"
#print(skip(up))
#p=""
#print(skip(p,up))
print(skipapple(up))