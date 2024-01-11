class TreeNode:
    def __init__(self,val):
        self.left= None
        self.right= None
        self.val =val
def sortedArrayToBst(nums):
    #base case if no elements simply return none
    if not nums:
        return None
        #picking the mid value 
    mid = len(nums)//2
    #making root value with the help of mid value
    root = TreeNode(nums[mid])
    #recursively calling root.left,right using some logic
    root.left = sortedArrayToBst(nums[:mid])
    root.right = sortedArrayToBst(nums[mid+1:])
    #finally returning root
    return root


#this function recursively  traverses the entire binary tree in pre order,printing the values of nodes as it visits them. the base case ensures recursion stops when it reaches leaf node(i.e a node with no left or right  child)
def PreorderTraversal(root):
    if root:
        #end = "" it is used to print values in the same line with the space seperated integers
        print(root.val, end= " ")
        #this step ensures left subtree of the current node is traversed in preorder,same with right and makes a recursive call 
        PreorderTraversal(root.left)
        PreorderTraversal(root.right)
n = int(input("enter no of elements"))
#splitting based on space
arr = list(map(int,input().split()))
root = sortedArrayToBst(arr)
PreorderTraversal(root)
