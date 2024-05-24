def selection(nums):
    for i in range(len(nums)):
        last=len(nums)-i-1
        maxindex=getmaxindex(nums,0,last)
        nums[maxindex],nums[last]=nums[last],nums[maxindex]
def getmaxindex(nums,start,end):
    max=start
    for i in range(start,end+1):
        if nums[max]<nums[i]:
            max=i 
    return max
nums=[5,1,4,3,2]
selection(nums)
print(nums)
