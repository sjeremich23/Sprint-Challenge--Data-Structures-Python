class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node:
        if value < self.value:
            # is there already a value at self.left
            # no ->
            if not self.left:
                self.left = BinarySearchTree(value)
                # after this ^, left is a new 'self' with it's own L/R
            # yes ->
            else:
                # then insert a the left
                self.left.insert(value)
        # if the value is greater:
        else:
            # is there a right?
            # if there is not a right then
            if not self.right:
                # add it to the right
                self.right = BinarySearchTree(value)
            else:
                # if then insert that value
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if the value is the target then return true
        if self.value == target:
            return True
        # go left
        # if target is less than self.value
        if target < self.value:
            # and it's not on the left
            if not self.left:
                # return false
                return False
            # otherwise
            else:
                # return the value of the target
                return self.left.contains(target)
        # go right
        else:
            # if it is not found
            if not self.right:
                # return false
                return False
            # otherwise
            else:
                # target is found and return that value
                return self.right.contains(target)

    # Return the maximum value found in the tree
    # self = root
    def get_max(self):
        # 1. if the tree is empty
        if not self:
            # returning None
            return None
        # 2. Otherwise, recur down the tree always going right
        # if you get to Null
        if not self.right:
            # then return last value found(we have found the value we need)
            return self.value
        # if there is something on the right, then return that value and call get max
        # this makes the function run again on the current node you are at
        # this is recursion
        return self.right.get_max()
