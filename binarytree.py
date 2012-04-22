
def createNewBinaryTree(centerpoint, s):
    """
    creates recursively a binary tree, centered on centerpoint from the set s
    """
    if len(s)==0:
        return BinaryTree(centerpoint)
    elif len(s) ==1:
        b = BinaryTree(centerpoint)
        b.setChildren(createNewBinaryTree(s.pop(), s), None)
        return b
    
    leftpoint = s.pop()
    rightpoint = s.pop()
    leftset = set()
    rightset = set()
    for p in s:
        if leftpoint.dist(p)<rightpoint.dist(p):
            leftset.add(p)
        else:
            rightset.add(p)
    b = BinaryTree(centerpoint)
    b.setChildren(createNewBinaryTree(leftpoint, leftset), createNewBinaryTree(rightpoint, rightset))
    return b

class BinaryTree:
    
    def __init__(self, v):
        self.val = v
        self.isLeaf = True
        self.children=(None, None)
        
    def search(self, e):
        if self.val == e or self.isLeaf:
            return self.val
        
        if self.isLeaf == True:
            return self.val
        else:
            return self.getNearestChild(e).search(e)
        
    def getNearestChild(self, e):
        (c0, c1) = self.getCosts(e)
        if c0<c1:
            return self.children[0]
        else:
            return self.children[1]
        
    def getCosts(self, e):
        return (e.dist(self.children[0].val), e.dist(self.children[1].val))
    
    def setChildren(self, left, right):
        self.isLeaf=False
        self.children = (left, right)
