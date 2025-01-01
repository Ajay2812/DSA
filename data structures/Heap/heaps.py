#build min heap using heapify
#time:O(n),space:O(1)

A=[-4,3,1,0,2,5,10,8,12,9]
import heapq

heapq.heapify(A)
print(A)


#push ele :O(log n)
heapq.heappush(A,-2)
#print(A)


#extract min : O(log n)
minn=heapq.heappop(A)
#print(A,minn)


#Heap Sort 
#time complexity:O(nlog n),space:O(n)

def heapsort(nums):
    heapq.heapify(nums)
    l=len(nums)
    new_list=[0]*l
    for i in range(l):
        minn=heapq.heappop(nums)
        new_list[i]=minn
    return new_list

#print(heapsort([2,1,9,8,34,6,5]))


#MAX HEAP
B=[-4,3,1,0,2,5,10,8,12,9]

n=len(B)
for i in range(n):
    B[i]=-B[i]
heapq.heapify(B)

#print(B)

largest=-heapq.heappop(B)
#print(B,largest)

#push negative numbers inorder to push into max heap

heapq.heappush(B,-7)

#print(B)


#Build heap from scratch time:O(n log n)

C=[-5,4,2,1,7,0,3]
heap=[]
for x in C:
    heapq.heappush(heap,x)
    #print(heap,len(heap))
#print(heap)


a=[5,5,4,3,4,3,4,3,3,4,4,3,3]
from collections import Counter
c=Counter(a)
heap=[]
heap1=[]
for k,v in c.items():
    heapq.heappush(heap,(k,v))
    heapq.heappush(heap1,(v,k))

print(heap)
print(heap1)




