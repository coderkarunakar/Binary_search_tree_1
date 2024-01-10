#Binary_Search_Tree
#search_node_in_tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#creating a function which basically tells wheather data is there or not in the node
def search(root,x):
    #base case if empty tree then simply return false 
    if root == None:
        return False
    if root.data == x:
        return True
        #x is smaller so every thing will be on left side
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.right,x)


def  printelements_in_range(root,k1,k2):
    if root == None:
        return 
        #it explores right subtree
    if root.data > k2:
         printelements_in_range(root.left,k1,k2)
         #it explores left subtree
    elif root.data < k1:
         printelements_in_range(root.right,k1,k2)
         #here printing occurs because it ensures only the nodes with in the specified range are printed,it avoids printing values that fall outside the specifed range k1,k2
    else:
        #after 
        print("the elements are",root.data)
        printelements_in_range(root.left,k1,k2)
        printelements_in_range(root.right,k1,k2)


def printTreeDetail(root):
    if root == None:
        return
    print(root.data,end=':')
    if root.left != None:
        print("L",root.left.data,end=',')
    if root.right != None:
        print('R',root.right.data,end='')
    print()
    printTreeDetail(root.left)
    printTreeDetail(root.right)

import queue
def TakeLevelWiseTreeInput():
    #importing the queue value
    q=queue.Queue()
    print("enter root")
    #taking the input data 
    rootData = int(input("enter root"))
    #if entered is - 1 i.e empty so return none
    if(rootData  == -1):
        return None
        #if not -1 then assigning to root value
    root = BinaryTreeNode(rootData)
    #we are adding it to the queue we use put method to append into queue
    q.put(root)
    #traversing if q is not empty
    while(not(q.empty())):
        #getting the current node value by using .get() in queue
        current_node = q.get()
        print("enter the left child of",current_node.data)
        leftchildData = int(input())
        if leftchildData!= -1:
            #assigning it to the leftchild
            leftchild = BinaryTreeNode(leftchildData)
            #assingning leftchild to current_node.left value
            current_node.left = leftchild
            #assigning leftchild to queue
            q.put(leftchild)

        print("enter the right child of ",current_node.data)
        rightchildData = int(input())
        if rightchildData!= -1:
            rightchild = BinaryTreeNode(rightchildData)
            current_node.right =rightchild
            q.put(rightchild)
    return root
root = TakeLevelWiseTreeInput()
printTreeDetail(root)
search(root,5)

printelements_in_range(root,20,50)
