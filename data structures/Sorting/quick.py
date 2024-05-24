def quick(nums,l,h):
    if l>=h:
        return
    s=l
    e=h
    m=s+(e-s)//2
    pivot=nums[m]
    while s<=e:
        while nums[s]<pivot:
            s+=1
        while pivot<nums[e]:
            e-=1
        if s<=e:
            temp=nums[s]
            nums[s]=nums[e]
            nums[e]=temp
            s+=1
            e-=1
    quick(nums,l,e)
    quick(nums,s,h)
arr=[5,3,4,1,2]
quick(arr,0,len(arr)-1)
print(arr)

    