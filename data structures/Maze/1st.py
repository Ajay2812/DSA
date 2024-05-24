def maze(r,c):
    if r==1 or c==1:
        return 1
    right=maze(r,c-1)
    down=maze(r-1,c)
    return right+down


def path(p,r,c):
    if r==1 and c==1:
        print(p)
        return 
    if r>1:
        path(p+'D',r-1,c)
    if c>1:
        path(p+'R',r,c-1)

#path("",3,3)


def listpath(p,r,c):

    if r==1 and c==1:
        l=[]
        l.append(p)
        return l
    li=[]
    if r>1:
        li.extend(listpath(p+'D',r-1,c))
    if c>1:
        li.extend(listpath(p+'R',r,c-1))
    return li

def listpathdia(p,r,c):

    if r==1 and c==1:
        l=[]
        l.append(p)
        return l
    li=[]
    if r>1:
        li.extend(listpathdia(p+'V',r-1,c))
    if c>1:
        li.extend(listpathdia(p+'H',r,c-1))
    if r>1 and c>1:
        li.extend(listpathdia(p+'D',r-1,c-1))
    return li


def pathrestrictions(p,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return 
    if maze[r][c]==False:
        return
    if r<len(maze)-1:
        pathrestrictions(p+'D',maze,r+1,c)
    if c<len(maze[0])-1:
        pathrestrictions(p+'R',maze,r,c+1)

#maze=[[True,True,True],[True,False,True],[True,True,True]]
#pathrestrictions("",maze,0,0)
      
    
    
