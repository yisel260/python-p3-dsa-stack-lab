class Stack:


    def __init__(self, items = [], limit = 100):
       self.dictionary ={}
       for item in items:
           self.dictionary[item] = True
       self.items = items 
       self.limit = limit 

    def isEmpty(self):
        return len(self.dictionary) == 0
          

    def push(self, item):
        if len(self.dictionary) < self.limit:
            self.dictionary[item] = True  
            self.items.append(item) 
            return self
        else:
            print("Stack is already full")
            return False

    def pop(self):
        if self.items:
            item = self.items.pop()
            self.dictionary.pop(item, None)
            return item
        else:
           return None

    def peek(self):
        pass
    
    def size(self):
       return len(self.dictionary)

    def full(self):
        return len(self.dictionary) == self.limit 


    def search(self, target):
       if target in self.dictionary:
           position = len(self.items) - self.items.index(target) - 1
           return position
       else:
        return -1