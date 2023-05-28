'''
1. what is stack?
LIFO
2. what are applications of stack?
3. Implementation
- push
-pop

'''

class stack:
    def __init__(self) -> None:
        self.list=[]
    
    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()

instance=stack()
instance.push(1)
instance.push(2)
instance.push(3)
instance.push(4)
print(instance.pop())
# print(instance.list)


