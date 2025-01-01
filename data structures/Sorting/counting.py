#time complexity:O(k+n)

#It is efficient when max in arrays is not so big



def counting(nums):
    m=max(nums)
    count=[0]*(m+1)
    for n in nums:
        count[n]+=1
    i=0
    for c in range(m+1):
        while count[c]>0:
            nums[i]=c
            i+=1
            count[c]-=1
A=[5,4,2,1,3,7,2,2]
counting(A)
print(A)