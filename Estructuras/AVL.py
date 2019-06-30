class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None
        self.height = None

class AVL_Tree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None
    
    def _find(self, value, node):
        if node == None:
            return None
        elif value == node.value:
            return node
        elif value < node.value and node.left != None:
            return self._find(value, node.left)
        elif value > node.value and node.right != None:
            return self._find(value, node.right)

    def find(self, value):
        if self.empty():
            return None
        else:
            return self._find(value, self.root)

    def insert(self,root,key):
        if not root:
            return Node(key)
        elif key < root.value:
            root.left= self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)
        
        root.height = 1 + max(self.getHeight(root.left)
        balance= self.getBalance(root)

        if balance > 1 and key < root.left.value:
            return self.rightRotate(root)

        elif balance < -1 and key > root.right.value:
            return self.leftRotate(root)

        elif balance > 1 and key > root.left.value:
            root.left= self.leftRotate(root.left)
            return self.rightRotate(root)

        elif balance < -1 and key < root.right.value:
            root.right= self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def leftRotate(self, z):
        y= z.right
        T2= y.left

        y.left= z
        z.right= T2
        
        z.height= 1+max(self.getHeight(z.left))
        self.getHeight(z.right)
        y.height= 1+max(self.getHeight(y.left))
        self.getHeight(y.right)

        return y

    def getHeight(self,current):
        if current == None:
            return height
            
        left_height = self._tree_height(current.left, height+1)
        right_height = self._tree_height(current.right, height+1)
        return max(left_height, right_height)

    def in_order(self, node): 
        if node==None:
            pass
        else:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    def post_order(self, node): 
        if node==None:
            pass
        else:
            self.in_order(node.left)
            self.in_order(node.right)
            print(node.value)

    def pre_order(self, node): 
        if node==None:
            pass
        else:
            print(node.value)
            self.in_order(node.left)
            self.in_order(node.right)
    
    def _leaf_number(self):
        if root.empty():
            return None
        elif root.left==None and root.right==None:
            print("Solo hay raiz")    
        else:
            return leaf_number(root)

    def leaf_number(self,node): #Numero de Hojas
        if node.left==None and node.right==None:
                leafcounter+=1
            self.leaf_number(node.left)
            self.leaf_number(node.right)



    def _tree_height(self, current, height):
        if current == None:
            return height
        left_height = self._tree_height(current.left, height+1)
        right_height = self._tree_height(current.right, height+1)
        return max(left_height, right_height)

    def tree_height(self): 
        if self.empty():
            return 0
        else:
            return self._tree_height(self.root, 0)

    def node_height(self, value): 
        node = self.root
        height = 0
        if self.find(value):
            height += 1
            while node.value != value:
                if value < node.value:
                    node = node.left
                else:
                    node = node.right
                height += 1
            return height
        else:
            return False

    def find_minimum(self): 
        if self.empty():
            return None
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return current

    def find_maximum(self): 
        if self.empty():
            return None
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return current

    def delete(self, value): 
        if self.empty():
            return None
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n): # Return the number of childrens of the node to be deleted
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = node.parent # Get the parent of the node to be deleted
        node_children = number_children(node)

        # Case 1: Deleting a node without childrens
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if node.left != None:
                child = node.left
            else:
                child = node.right

            # Replace the node to be deleted with its child
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            # Change the parent of the child
            child.parent = node_parent
        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = min_value_node(node.right) # Get the inorder successor of the deleted node
            node.value = successor.value # Copy the value
            self.delete_node(successor)
        
        node.height = 1 + max(self.getHeight(node.left)
        self.getHeight(node.right)

        balance = self.getbalance(node)

        if balance > 1 and node.value < node.left.value:
           return self.rightRotate(node)

        if balance < -1 and node.value > node.right.value:
            return self.leftRotate(node)

        if balance > 1 and node.value > node.left.value:
            node.left= self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and node.value < node.right.value:
            node.right= self.rightRotate(node.right)
            return self.leftRotate(node)
        return node
