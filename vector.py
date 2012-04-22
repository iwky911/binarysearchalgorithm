

class Vector:
    distbuff = [range(25) for i in range(25)]
    
    def __init__(self, v):
        self.values = v
    
    def dist(self, v):
        imax = len(self.values)
        jmax = len(v.values)
        if len(v.values)<len(self.values):
            return v.dist(self)
        
        t = Vector.distbuff
        # t[i][j] contains the dist between the ith first elements of self and the jth first elements of v
        # t[i][j] equals the 
        
        for i in range(1,imax+1):
            for j in range(1,jmax+1):
                t[i][j] = min(t[i-1][j]+1, t[i][j-1]+1, t[i-1][j-1]+ (0 if self.values[i-1]==v.values[j-1] else 1))
        return t[imax][jmax]
                
    def __repr__(self):
        return self.values
