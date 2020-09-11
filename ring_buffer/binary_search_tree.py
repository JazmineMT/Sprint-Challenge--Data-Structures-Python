from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.storage = Queue()

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            #check if the node to the left is None
            if self.left:
                # if yes -> insert a new node here
                self.left.insert(value)
            else:
                #if not insert to the left
                self.left = BSTNode(value)
        else:
            # check if node to the right is None
            if self.right:
                #if yes --> insert a new Node here
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
                
    # Return True if the tree contains the value
    # False if it does not             
    def contains(self, target):
        # check is target value is greater than or equal to root 
        if target == self.value:
            #if true return True
            return True 
        #check is target value is greater than self value
        if target > self.value:
            # loop through the right side and reture false if it doesn't match - when you reach the end return true 
            while self.right.value != target:
                    return False
                
            return True 
        # if the target value is less than the root value we go through the left side     
        else:
            while self.left.value != target:
                    return False
            return True
        # better way to do this 
            #if target > self.value:
                #if self.right is None:
                    #return false
                #else:
                    #return self.right.contains(target)
            #if target < self.value:
                #if self.left is None:
                    #return False
                #else:
                    #self.left.contains(target)
                 
 

    # Return the maximum value found in the tree
    def get_max(self):
        #check if there is no right 
        if self.right == None:
            #if there is none return the root value
            return self.value
        #decalre the variable we want to change
        self = self  
        # run this loop until there is nothing to the right
        while self.right != None:
            # each time change the right side to the new self 
            self  = self.right 
        # once we get to the end of the loop return the final value 
        return self.value

        # better way to do this 
            # else:
            #     return self.right.get_max()
     

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.right:
            self.right.for_each(fn)
            
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        #base case
        if self.left:
            self.left.in_order_print()
        
        print(self.value)
            
        if self.right:
            self.right.in_order_print()
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    #use queue we made earlier in the week
    # and a while loop
    def bft_print(self):
        q = Queue()
        
        q.enqueue(self.value)
        
        while q.size > 0 :
            currentnode = q.dequeue()
            print(currentnode.value)
            
            if currentnode.left:
                q.enqueue(currentnode.left)
            if currentnode.right:
                q.enqueue(currentnode.right)
     