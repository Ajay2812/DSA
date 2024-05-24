def mergesort(nums):
    if len(nums)==1:
        return nums
    mid=len(nums)//2
    left=mergesort(nums[:mid])
    right=mergesort(nums[mid:])
    return merge(left,right)

def merge(first,second):
    l=[0]*(len(first)+len(second))
    i=0
    j=0
    k=0
    while i<len(first) and j<len(second):
        if first[i]<second[j]:
            l[k]=first[i]
            i+=1
        else:
            l[k]=second[j]
            j+=1
        k+=1
    while i<len(first):
        l[k]=first[i]
        i+=1
        k+=1
    while j<len(second):
        l[k]=second[j]
        j+=1
        k+=1
    return l

nums=[8,2,7,4,5,1,6]
ans=mergesort(nums)
print(ans)