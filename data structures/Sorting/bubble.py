def bubble(nums):
    for i in range(len(nums)):
        swapped=False
        for j in range(1,len(nums)-i):
            if nums[j]<nums[j-1]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
                swapped=True

        if not swapped:
            break

nums=[5,3,1,2,4]
bubble(nums)
print(nums)
               