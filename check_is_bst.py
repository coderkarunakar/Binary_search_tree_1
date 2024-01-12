#check is bst or not
#Binary_Search_Tree
#search_node_in_tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



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



    #for better understanding please take a look inside notes as well this logic is well explained there
#taking min value and max value from the left subtree 
def minTree(root):
    #base case if the root is none then return 100000 Note:this is for left subtree
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin= minTree(root.right)
    return min(leftMin,rightMin,root.data)
    #finding max value from the right subtree
def maxTree(root):
    #    #base case if the root is none then return -100000 Note:this is for right subtree
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax,rightMax,root.data)
    
def isBst(root):
    #base case if the root itself is empty then it is a bst 
    if root == None:
        return True
        #calling above created function and checking leftmax,right min vlaue
    leftmax =maxTree(root.left)
    rightmin = minTree(root.right)
    #checking condition
    if root.data > rightmin or root.data <= leftmax:
        return False
    #if above one is failed then checking inside leftsubtree,right subtree which calls above 2 created functions as well and finally returns left,right bst
    isLeftBST = isBst(root.left)
    isRightBST = isBst(root.right)
    return isLeftBST and isRightBST

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


if isBst(root):
    print("The tree is a Binary Search Tree (BST).")
else:
    print("The tree is not a Binary Search Tree (BST).")


