class MyStack:

    def __init__(self):
        self.list1 = []

    def push(self, x: int) -> None:
        self.list1.append(x)
        for z in range(len(self.list1) - 1):
            self.list1.append(self.list1.pop(0))

    def pop(self) -> int:
        return self.list1.pop(0)
    
    def top(self) -> int:
        if self.empty():
            return 0
        else:
            return self.list1[0]

    def empty(self) -> bool:
        return (not self.list1)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()