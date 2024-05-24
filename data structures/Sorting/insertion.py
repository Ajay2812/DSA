def insertion(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,0,-1):
            if nums[j]<nums[j-1]:
                nums[j-1],nums[j]=nums[j],nums[j-1]


nums=[5,9,10,4,2]
insertion(nums)
print(nums)