def allpaths(p,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return
    if maze[r][c]==False:
        return
    #consider this path in my block
    maze[r][c]=False
    if r<len(maze)-1:
        allpaths(p+'D',maze,r+1,c)
    if c<len(maze[0])-1:
        allpaths(p+'R',maze,r,c+1)
    if r>0:
        allpaths(p+'U',maze,r-1,c)
    if c>0:
        allpaths(p+'L',maze,r,c-1)
    #this is where fn is over
    #so before the fn gets removed ,also remove the changes made during the fn
    maze[r][c]=True


maze=[[True,True,True],[True,True,True],[True,True,True]]
allpaths("",maze,0,0)

