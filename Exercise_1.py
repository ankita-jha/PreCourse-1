class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
  # Space Complexity: O(n)
  # Time : O(n)
     def __init__(self):
         self.arr=[]
         self.top=-1
         
     def isEmpty(self):
       if len(self.arr)==0:
         return True
       return False
         
     def push(self, item):
       
       self.arr.append(item)
       self.top+=1
       
         
     def pop(self):
       if self.isEmpty()==True:
         return "stack underflow"
       element=self.arr[self.top]
       self.top-=1
       return element
        
        
     def peek(self):
       if self.isEmpty()==True:
         return "stack underflow"
       return self.arr[top]
        
     def size(self):
       return self.top+1
         
     def show(self):
       return self.arr.copy()
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
