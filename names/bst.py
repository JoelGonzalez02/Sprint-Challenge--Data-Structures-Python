
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):

        if self.value > value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        elif self.value <= value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        

        if self.value <= target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

