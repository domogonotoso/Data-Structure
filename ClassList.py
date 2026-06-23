class ClassL(list):
    def __init__(self, li):
        super().__init__(li)

    def Insert(self, pos, e):
        b = self[:pos]
        a = self[pos:]
        b.append(e)
        self[:] = b + a
    def Delete(self, pos):
        b = self[:pos]
        a = self[pos + 1:]
        self[:] = b + a
    def isFull(self):
        # for a in self:
        #     if a == None:
        #         return False
        #     else :
        #         return True
        return None not in self   
    def isEmpty(self):
        for i in self:
            if self[i] != None :
                return True
            else :
                return False
        # return all(x is None for x in self)
   
    def getEntry(self, pos):
        try: a = self[pos]
        except: a = None
        return a
    def Size(self):
        n = 0
        for i in range(len(self)):
            if self[i] != None:
                n += 1
        return n
    def Clear(self):
        # super().__init__([]*len(self))
        self[:] = []
    def Find(self, item):
        for i in range(len(self)):
            if self[i] == item:
                return i
    def Replace(self, pos, item):
        self[pos] = item
    def Append(self, e):
        for i in range(len(self)):
            if self[i] == None:
                self[i] = e
                break
    def Enu(self): #,pos
        li = [(i, self[i]) for i in range(len(self)) ]
        return li