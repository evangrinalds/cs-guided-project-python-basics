class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        
        while left.isEmpty() is False:
            popped = left.pop()
            print(popped)
            right.push(popped)
            
        ret = 0
        
        if right.isEmpty() is False:
            ret = right.pop()
        
        while right.isEmpty() is False:
            popped = right.pop()
            left.push(popped)
            
        return ret
            
    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans
