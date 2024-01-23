class Node:
    def __init__(self,key):
        self.leftChild = None
        self.rightChild = None
        self.val = key
    def insert(self,data):
        if self.val:
            if data <self.val:
                if self.leftChild is None:
                    self.leftChild = Node(data)
                else:
                    self.leftChild.insert(data)
            elif data > self.rightChild:
                if self.rightChild is None:
                    self.rightChild = Node(data)
                else:
                    self.rightChild.insert(data)
            else:
                self.val = data
    def search(self,key):
        if key <self.data:
            if self.leftChild is None:
                return str(key)+"Not Found"
            return self.leftChild.search(key)
        if key >self.data:
            if self.rightChild is None:
                return str(key)+"Not Found"
            return self.rightChild.search(key)                                          
        else:
            print(str(self.data)+"is found")

    def printTree(self,prefex):
        if self is None:
            return
        self.leftChild.printTree()
                
def InorderTravesal(root):
    if root:
        InorderTravesal(root.leftChild)
        print(root.val)
        InorderTravesal(root.rightChild)
def PreorderTravesal(root):
    if root:
        print(root.val)
        PreorderTravesal(root.leftChild)
        PreorderTravesal(root.rightChild)
def PostorderTravesal(root):
    if root:
        PostorderTravesal(root.leftChild)
        PostorderTravesal(root.rightChild)
        print(root.val)
if __name__ == "__main__":
    root = Node(3)
    root.leftChild = Node(26)
    root.rightChild = Node(42)
    root.leftChild.leftChild = Node(54)
    root.leftChild.rightChild = Node(65)
    root.rightChild.leftChild = Node(12)
    InorderTravesal(root)


class BStree:
    def __init__(self):
        self._root = None
        self._size = 0
    
    def __len__(self):
        return self._size
class BStreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right  = None
    def _bstSearch(self,subtree,target):
        if subtree is None:
            return None
        elif target <subtree.key:
            return self._bstSearch(subtree.left,target)
        elif target >subtree.key:
            return self._bstSearch(subtree.right,target)
        else:
            return subtree

