from priority_queue import qu

class tamsek(qu):
    def __init__(self, miro, start, end):
        super().__init__([(start, self.d(start, end))])

        self.miro = miro
        self.start = start
        self.end = end
        self.trajectory = [start]
        self.finish = False

    def chek(self, i, j):
        if (i, j) == self.end : self.finish = True; return 1
        if self.miro[i][j] == 0 and \
            (i, j) not in self.trajectory and \
            i != -1 and j != -1:
            
            self.Enqueue((i, j), self.d((i,j) , self.end))
            self.trajectory.append((i,j))
    def process(self):
        n = 0
        while True:
            n += 1
            point = self.dequeue()
            x = point[0]
            y = point[1]
            try:
                for p, q in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    self.chek(x+p, y+q)
                    if self.finish == True:print(n); print(x+p, y+q); return True
            
            except:
                pass
            
    def d(self, a, b):
        return ((a[0] - b[0])**2 + (a[1] - b[1]) **2)**(1/2)


            


        
    