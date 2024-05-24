def subseq(p,up):
    if not up:
        print(p)
    ch=up[0]
    subseq(p,up[1:])
    subseq(p+ch,up[1:])

def subseqlist(p,up):
    if not up:
        l=[]
        l.append(p)
        return l
    ch=up[0]
    left=list(subseqlist(p,up[1:]))
    right=list(subseqlist(p+ch,up[1:]))
    left.extend(right)
    return left

def subseqAscii(p,up):
    if not up:
        l=[]
        l.append(p)
        return l
    ch=up[0]
    first=list(subseqAscii(p,up[1:]))
    second=list(subseqAscii(p+ch,up[1:]))
    last=list(subseqAscii(p+str(ord(ch)),up[1:]))
    first.extend(second)
    first.extend(last)
    return first
p=""
up="abc"
print(subseqlist(p,up))