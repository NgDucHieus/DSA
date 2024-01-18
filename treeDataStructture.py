class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursiv(value,self.root)
        
    def _insert_recursiv(self,value,current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursiv(value,current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else: 
                self._insert_recursiv(value,current_node.right)
        else:
            pass
    def inorder_traversal(self,node):
        result =[]
        if node:
            result += self.inorder_traversal(node.left)
            result.append(node.value)
            result += self.inorder_traversal(node.right)
        return result
    # def find_value(self,input_number):
    #     if input_number < self.root.value:
    #         if self.root.left is None

    a = 0 
    b = 0
        

tree = BinaryTree()
value =[23,9,75,6,2,1,4,23,44,5]
for value in value:
    tree.insert(value)
print(tree.inorder_traversal(tree.root))
print(tree.root.value)
        
            
print(9999+9999999)
class ListNode:
    def __init__(self,val = 0,nextnode = None) :
        self.val = val
        self.next = nextnode
    
l1= ListNode(10)
l2 = ListNode(200)
l1.next = l2
# def addTwoNumber(l1:Optional[ListNode]):
#     pass
# addTwoNumber(l1 = l1)



def from_linked_list_to_number(l):
        index = 0
        num = 0
        while l != None:
            num += 10**index*l.val
            index+=1
            l = l.next
        return num
# def from_num_to_linked_list(num):
def insert(num,l):
    curent_Node = l
    

a = 1111111
print(len(a))

