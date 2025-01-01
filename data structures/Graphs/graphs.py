#Array of Edges (Directed) [start,end]

n=8  #edges
A=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

#Adjacency Matrix
M=[]
for i in range(n):
    M.append([0]*n)
for u,v in A:
    M[u][v]=1
    #For undirected graph use M[v][u] =1 also
#print(M)

#By using dict

from collections import defaultdict

D=defaultdict(list)

for u,v in A:
    D[u].append(v)
    #For undirected graph use D[v].append(u) also

#print(D)