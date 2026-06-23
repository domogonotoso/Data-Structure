class qu:
    def __init__(self,li):
        self.li = li if li is not None else []

    def Enqueue(self, e, p):
        print("Enqueue :", (e, p))
        self.li.append((e, p))
    def dequeue(self):
        ind = 0
        min = self.li[0][1]
        for i in range(len(self.li)):
            if self.li[i][1] < min:
                ind = i
                min = self.li[i][1]
        r = self.li[ind][0]
        print("dequeue :", self.li[ind])
        self.li.pop(ind)
        return r
    def isEmpty(self):
        if len(self.li) == 0:
            return True
        else : return False
    def isFull(self):
        pass
    def peek(self):
        return self.li[0]
    