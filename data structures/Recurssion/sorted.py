def sorted(nums,i):
    if i==len(nums)-1:
        return True
    else:
        return nums[i]<nums[i+1] and sorted(nums,i+1)
    
nums=[1,2,3,4,8,6,7]
print(sorted(nums,0))
