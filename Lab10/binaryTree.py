# ----------------------------------------------------
# Lab 10, Binary Trees
#
#
# Purpose of code: These are three exercises of Binary trees
#
#
# Author: Yi Yang
# Collaborators/references: C175-13-F20-Trees.pdf from eclass
# ----------------------------------------------------


class BinaryTree:
    def __init__(self, rootElement):
        self.key = rootElement
        self.left = None
        self.right = None
        
    '''getters'''
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getKey(self):
        return self.key
    
    '''setters'''
    def setKey(self,key):
        self.key=key
        
    def setLeft(self,left):
        self.left=left        
  
    def setRight(self,right):
        self.right=right
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
  
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t 
            
    def _strHelper(self):
        """Returns list of strings,  total width of the tree, position of the middle node and the height"""
        # Base case, no child.
        if self.getLeft() == None and self.getRight() == None:
            row = '%s' % self.key
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % self.key
        keyStrLength = len(keyStr)
        # Case 1: only have left child
        if self.getLeft() != None and self.getRight() == None:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength) * ' '
            shiftedRows = [row + keyStrLength * ' ' for row in leftRows]
            return [firstRow, secondRow] + shiftedRows, leftWidth + keyStrLength,leftWidth + keyStrLength // 2, leftHeight + 2

        # Case 2: only have right child
        elif self.getLeft() == None and self.getRight() != None:
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper()
            firstRow = keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = (keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedRows = [keyStrLength * ' ' + row for row in rightRows]
            return [firstRow, secondRow] + shiftedRows, rightWidth + keyStrLength,keyStrLength // 2, rightHeight + 2, 

        # Two children.
        else:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper() 
          
    
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            #append a few rows to fill in the blanks in the bottom, so that left and right lists are of the length
            if leftHeight < rightHeight:
                leftRows += [leftWidth * ' '] * (rightHeight - leftHeight)
            else:
                rightRows += [rightWidth * ' '] * (leftHeight - rightHeight)
            pairedRows = zip(leftRows, rightRows)
            rows = [firstRow, secondRow] + [i + keyStrLength * ' ' + j for i, j in pairedRows]
            return rows, leftWidth + rightWidth + keyStrLength,  leftWidth + keyStrLength // 2,max(leftHeight, rightHeight) + 2
    
    
    def __str__(self):
        rows, _, _, _ = self._strHelper()
        result = ''
        for row in rows:
            result += row + "\n"
        return result
    


################################################################################
##  EXERCISE 1
################################################################################    

def preorder(tree):
    '''
    print the value of a tree in a Preorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''

    if tree != None:
        print(tree.getKey())
        preorder(tree.getLeft())
        preorder(tree.getRight())

def inorder(tree):
    '''
    print the value of a tree in an Inorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''

    if tree != None:
        inorder(tree.getLeft())
        print(tree.getKey())
        inorder(tree.getRight())

def postorder(tree):
    '''
    print the value of a tree in a postorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''

    if tree != None:
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print(tree.getKey())
        
################################################################################
##  EXERCISE 2
################################################################################ 


def findMinKey(tree):
    '''
    find the minimum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''


    if tree != None:
        min = tree.getKey()
        temp1 = findMaxKey(tree.getLeft())
        temp2 = findMaxKey(tree.getRight())

        if temp1 != None and temp1 < min:
            min = temp1
        if temp2 != None and temp2 < min:
            min = temp2

        return min


def findMaxKey(tree):
    '''
    find the maximum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''

    if tree != None:
        max = tree.getKey()
        temp1 = findMaxKey(tree.getLeft())
        temp2 = findMaxKey(tree.getRight())

        if temp1 != None and temp1 > max:
            max = temp1
        if temp2 != None and temp2 > max:
            max = temp2

        return max


################################################################################
##  EXERCISE 3
################################################################################ 

def buildTree(inOrder, preOrder): 
    '''
    Build a binary tree based on given Inorder and PreOrder traversals
    
    Parameters:
        - inOrder,preOrder (list of numbers)
    
    Returns: a BinaryTree object
    '''

    #base case:
    if len(preOrder) == 0 or len(inOrder) == 0:
        return
    
    #get the root value
    rootValue = preOrder[0]
    
    #find the index of root value in Inorder traversal
    rootValueIndex = inOrder.index(rootValue)

    #build the tree recursively
    tree = BinaryTree(rootValue)

    tree.left = buildTree(inOrder[:rootValueIndex], preOrder[1:rootValueIndex + 1])
    tree.right = buildTree(inOrder[rootValueIndex + 1:], preOrder[rootValueIndex + 1:])

    return tree


################################################################################
##  Test your functions: you are encouraged to add other tests as well
################################################################################ 
def main():
    tree = BinaryTree(1)
    tree.insertLeft(2)
    tree.insertRight(7)
    tree.getLeft().insertLeft(3)
    tree.getLeft().insertRight(6)
    tree.getLeft().getLeft().insertLeft(4)
    tree.getLeft().getLeft().insertRight(5)
    tree.getRight().insertLeft(8)
    tree.getRight().insertRight(9)

    print("the tree:\n")
    print(tree)
    
    print("preorder traversal:")
    preorder(tree)
    print()
    print("inorder traversal:")
    inorder(tree)
    print()
    print("postorder traversal:")
    postorder(tree)
    print()

    print('Max value in tree:', findMaxKey(tree))
    print('Min value in tree:', findMinKey(tree))

    inor = [4,3,5,2,6,1,8,7,9]
    preor = [1,2,3,4,5,6,7,8,9]

    theTree = buildTree(inor,preor)
    
    print(theTree)
    
    inor2 = [3,2,4,1,5]
    preor2 = [1,2,3,4,5]

    theTree2 = buildTree(inor2,preor2)
    
    print(theTree2)  
    
    
if __name__ == "__main__":
    main()        