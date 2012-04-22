

distbuff = [range(70) for i in range(70)]

def dist(v1, v2):
    imax = len(v1)
    jmax = len(v2)
    if len(v2)<len(v1):
        return dist(v2, v1)
    
    t = distbuff
    # t[i][j] contains the dist between the ith first elements of v1 and the jth first elements of v2
    # t[i][j] equals the 
    
    for i in range(1,imax+1):
        for j in range(1,jmax+1):
            t[i][j] = min(t[i-1][j]+1, t[i][j-1]+1, t[i-1][j-1]+ (0 if v1[i-1]==v2[j-1] else 1))
    return t[imax][jmax]
