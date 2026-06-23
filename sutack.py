import ClassList 

class Sutack(ClassList.ClassL):
    def __init__(self, li):
        super().__init__(li)

    def Push(self, e):
        #self.append(e)
        print('push :', e)
        self.Insert(len(self), e)

    def Pop(self):
        tail = len(self) - 1
        p = self[tail]
        print('pop :', p)
        self.Delete(tail)
        return p

    # def IsFull(self):

    # def isEmpty(self):

    def Peek(self):
        return self[- 1] 

    # def Size(self):

    def Clear(self):
        super().__init__([])
