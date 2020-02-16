'''
Design a max stack that supports push, pop, top, peekMax and popMax.

    push(x) -- Push element x onto stack.
    pop() -- Remove the element on top of the stack and return it.
    top() -- Get the element on the top.
    peekMax() -- Retrieve the maximum element in the stack.
    popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:

    -1e7 <= x <= 1e7
    Number of operations won't exceed 10000.
    The last four operations won't be called when stack is empty.


'''

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.maxStack)==0:
            self.maxStack.append(x)
        elif self.maxStack[-1]<x:
            self.maxStack.append(x)
        else:
            self.maxStack.append(self.maxStack[-1])
            

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()
        
        
    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
    

    def peekMax(self) -> int:
        if len(self.maxStack)>0:
            return self.maxStack[-1]
        else:
            return None
        

    def popMax(self) -> int:
        
        n=self.maxStack.pop()
        
        tmp=[]
        while n!=self.stack[-1]:
            tmp.append(self.stack.pop())
            self.maxStack.pop()
        ret=self.stack.pop()
        for i in range(len(tmp)-1,-1,-1):
            self.push(tmp[i])
        return ret


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
