from vector import *
import sys

def createNewBinaryTree(s):
    center = s.pop()
    return createNewCenteredBinaryTree(center, s, sys.maxint)

def createNewCenteredBinaryTree(centerpoint, s, maxdist):
    """
    creates recursively a binary tree, centered on centerpoint from the set s
    """
    if len(s)==0:
        return BinaryTree(centerpoint, maxdist)
    elif len(s) ==1:
        b = BinaryTree(centerpoint, maxdist)
        b.setChildren(createNewCenteredBinaryTree(s.pop(), s), None)
        return b
    
    leftpoint = s.pop()
    rightpoint = s.pop()
    leftset = set()
    rightset = set()
    maxdistleft = 0
    maxdistright = 0
    for p in s:
        dleft = dist(p, leftpoint)
        dright = dist(p, rightpoint)
        if dleft< dright:
            leftset.add(p)
            maxdistleft = max(maxdistleft, dleft)
        else:
            maxdistright = max(maxdistright, dright)
            rightset.add(p)
    b = BinaryTree(centerpoint, maxdist)
    b.setChildren(createNewCenteredBinaryTree(leftpoint, leftset, maxdistleft), createNewCenteredBinaryTree(rightpoint, rightset, maxdistright))
    return b

class BinaryTree:
    
    def __init__(self, v, maxdist):
        self.val = v
        self.maxdist = maxdist
        self.isLeaf = True
        self.children=(None, None)
        
    def search(self, e):
        (c,v) = self.getMinDistance(e, sys.maxint, None)
        return v
        
    def getMinDistance(self, e, mincost, minval):
        if e == self.val:
            return (0, e)
        if self.isLeaf:
            c = dist(e,self.val)
            return (c,self.val) if c<mincost else (mincost, minval)
        (c0, c1) = self.getCosts(e)
        #(v0, v1) = getCost(minval)
        
        order = (0,1) if c0<=c1 else (1,0)
        for i in order:
            if self.children[i].maxdist+mincost>=c0:
                (c, v) = self.children[i].getMinDistance(e, mincost, minval)
                if c< mincost:
                    (mincost, minval) = (c,v)
        
        return (mincost, minval)
        
    def getNearestChild(self, e):
        (c0, c1) = self.getCosts(e)
        if c0<c1:
            return self.children[0]
        else:
            return self.children[1]
        
    def getCosts(self, e):
        print self.children
        return (dist(e, self.children[0].val), dist(e, self.children[1].val) if self.children[1] != None else sys.maxint)
    
    def setChildren(self, left, right):
        self.isLeaf=False
        self.children = (left, right)
