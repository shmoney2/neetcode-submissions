class Listnode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home_node = Listnode(homepage)
        self.head = self.home_node
        self.curr = self.home_node
    def visit(self, url: str) -> None:
        x = Listnode(url)
        self.curr.next = x
        x.prev = self.curr
        self.curr = self.curr.next


    def back(self, steps: int) -> str:
        for x in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
        return self.curr.val

    def forward(self, steps: int) -> str:
        for x in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)