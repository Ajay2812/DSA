from collections import defaultdict

D=defaultdict(list)
A=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

for u,v in A:
    D[u].append(v)

print(D)
def dfs_rec(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_rec(nei_node)


source=0
seen=set()
seen.add(source)
#dfs_rec(source)


#Iterative Dfs

s=0
visit=set()
visit.add(s)

stack=[source]
while stack:
    node=stack.pop()
    print(node)
    for neig_node in D[node]:
        if neig_node not in visit:
            visit.add(neig_node)
            stack.append(neig_node)
    
