class MinStack:

    def __init__(self):
        self.lst = []
        

    def push(self, val: int) -> None:
        self.lst.append(val)
        

    def pop(self) -> None:
        self.lst.pop()        

    def top(self) -> int:
        n = len(self.lst)
        return self.lst[n-1]
        

    def getMin(self) -> int:
        tmp = []
        mini = self.lst[-1]

        while len(self.lst):
            mini = min(mini, self.lst[-1])
            tmp.append(self.lst.pop())

        while len(tmp):
            self.lst.append(tmp.pop())
        
        return mini
        
