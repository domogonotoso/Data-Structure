import ClassList 

class qu(ClassList.ClassL):
    def __init__(self,li):
        super().__init__(li)

    def Enqueue(self, e):
        print('Enqueue :', e)
        self.append(e)
    def dequeue(self):
        r = self[0]
        print('dequeue :', r)
        self.Delete(0)
        return r
    
    def isEmpty(self):
        if len(self) == 0:
            return True
        else : return False
    def isFull(self):
        pass
    def peek(self):
        return self[0]
    