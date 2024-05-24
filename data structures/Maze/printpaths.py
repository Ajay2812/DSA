def printpaths(p,maze,r,c,path,step):
    if r==len(maze)-1 and c==len(maze[0])-1:
        path[r][c]=step
        for nums in path:
            print(nums)
        print(p)
        print()
        return
    if maze[r][c]==False:
        return
    #consider this path in my block
    maze[r][c]=False
    path[r][c]=step

    if r<len(maze)-1:
        printpaths(p+'D',maze,r+1,c,path,step+1)
    if c<len(maze[0])-1:
        printpaths(p+'R',maze,r,c+1,path,step+1)
    if r>0:
        printpaths(p+'U',maze,r-1,c,path,step+1)
    if c>0:
        printpaths(p+'L',maze,r,c-1,path,step+1)
    #this is where fn is over
    #so before the fn gets removed ,also remove the changes made during the fn
    maze[r][c]=True
    path[r][c]=0


maze=[[True,True,True],[True,True,True],[True,True,True]]
#path=[[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
path=[[0,0,0],[0,0,0],[0,0,0]]
printpaths("",maze,0,0,path,1)

