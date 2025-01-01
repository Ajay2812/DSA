from collections import defaultdict
from collections import deque


D=defaultdict(list)
A=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]
for u,v in A:
    D[u].append(v)

source=0
seen=set()
seen.add(source)
q=deque()
q.append(source)
while q:
    node=q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)

