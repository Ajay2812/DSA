def searching(nums,target,i):
    if i==len(nums):
        return False
    else:
        return nums[i]==target or searching(nums,target,i+1)
    



def findindex(nums,target,i):
    if i==len(nums):
        return -1
    if nums[i]==target:
        return i
    else:
        return findindex(nums,target,i+1)


def findAllIndex(nums,target,i):
    if i==len(nums):
        return -1
    if nums[i]==target:
        l.append(i)
    findAllIndex(nums,target,i+1)

def allindices(nums,target,i,l):
    if i==len(nums):
        return l
    if nums[i]==target:
        l.append(i)
    return allindices(nums,target,i+1,l)
nums=2,6,12,23,34,6,3,7,6
target=6
l=[]
allindices(nums,target,0,l)
print(l)