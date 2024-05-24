def rotatedsearch(nums,target,s,e):
    if s>e:
        return -1
    m=s+(e-s)//2
    if target==nums[m]:
        return m
    if nums[s]<=nums[m]:
        if target>=nums[s] and target<nums[m]:
            return rotatedsearch(nums,target,s,m-1)
        else:
            return rotatedsearch(nums,target,m+1,e)
    if target >=nums[m] and target<=nums[e]:
        return rotatedsearch(nums,target,m+1,e)
    return rotatedsearch(nums,target,s,m-1)

nums=5,6,7,8,9,1,2,3
print(rotatedsearch(nums,1,0,len(nums)))
