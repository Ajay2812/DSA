def dominant(nums):
    if len(nums)==0:
        return -2
    s=0
    for i in range(len(nums)):
        if i==len(nums)-1 or nums[i]>max(nums[i+1:]):
            s+=nums[i]
    return s

nums=[52,66,64,32,60,50]
print(dominant(nums))