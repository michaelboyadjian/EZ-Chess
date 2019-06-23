from Queue import *

class tree:
    def __init__(self, x):
        self.store = [x, []]

    def AddSuccessor(self, x):
        self.store[1] = self.store[1] + [x]
        return True

    def GetSuccessors(self):
        return self.store[1]

    def Print_DepthFirst(self):
        self.Print_DepthFirst_helper("   ")
        return True

    def Print_DepthFirst_helper(self, prefix):
        print(prefix+str(self.store[0]))
        for i in self.store[1]:
            i.Print_DepthFirst_helper(prefix+"   ")
        return True

    def Get_LevelOrder(self):
        x = queue()
        x.enqueue(self.store)
        accum = []
        while True:
            y = x.dequeue()
            # y is a 2-list where y[0] = True/False
            # and y[1] is the actual dequeued value when y[0]=True
            if (y[0] == False):
                break
            else:
                v = y[1]
                accum = accum + [v[0]]
                for i in v[1]:
                    x.enqueue(i.store)
        return accum

