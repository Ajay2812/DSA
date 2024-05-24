def cyclic(nums):
    i=0
    while i<len(nums):
        correct=nums[i]-1
        if nums[i] != nums[correct]:
            nums[i],nums[correct]=nums[correct],nums[i]
        else:
            i+=1
nums=[5,1,3,4,2]
cyclic(nums)
print(nums)
