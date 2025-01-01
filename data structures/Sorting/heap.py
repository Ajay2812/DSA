import heapq



def heapsort(nums):
    heapq.heapify(nums)
    l=len(nums)
    new_list=[0]*l
    for i in range(l):
        minn=heapq.heappop(nums)
        new_list[i]=minn
    return new_list

print(heapsort([2,1,9,8,34,6,5]))