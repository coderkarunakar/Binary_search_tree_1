#check is bst or not
#Binary_Search_Tree
#search_node_in_tree
#bst2 improved solution
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

#improved submission for check bst
def isBST2(root):
    #if root is empty it is a bst only so we are returning max,min  ,bst is true
    if root == None:
        return 100000,-100000,True
        #we are getting this 6 values by recursion calls on roots left or roots right
    LeftMin,LeftMax,isLeftBst=isBST2(root.left)
    RightMin,RightMax,isRightBst=isBST2(root.right)
    #getting the min value among leftmax,leftmin,and root data similarly getting max value among them
    minimum = min(LeftMin,RightMin,root.data)
    maximum = max(RightMax,LeftMax,root.data)
    isTreeBST =True

    #2conditions we need to verify overall bst and leftsubtree ,and right subtree bst we need to ensure
    #this is the logic for BST
    if root.data <= LeftMax or root.data > RightMin:
        isTreeBST = False
    if not (isLeftBst) or not (isRightBst):
        isTreeBST = False
    return minimum,maximum,isTreeBST




#a big note in python if you want to return something you need to print it
#for bst

# root = TakeLevelWiseTreeInput()
# printTreeDetail(root)
# print(isBst(root))



#BST 2
root = TakeLevelWiseTreeInput()
printTreeDetail(root)
print(isBST2(root))




