# type: ignore
import sys

class Queue:
    def __init__(self):
        self.stack = []
        self.rstack = []

    def enqueue(self, val):
        self.stack.append(val)

    def peek(self):
        if self.rstack:
            return self.rstack[-1]

        for _ in range(len(self.stack)):
            x = self.stack.pop()
            self.rstack.append(x)
        
        return self.rstack[-1]

    def pop(self):
        if self.rstack:
            self.rstack.pop()
            return

        for _ in range(len(self.stack) - 1):
            x = self.stack.pop()
            self.rstack.append(x)

        self.stack.pop()

    def __str__(self):
        return str(self.stack)

def main():
    q = Queue()
    nops = int(sys.stdin.readline())
    for _ in range(nops):
        op = sys.stdin.readline().split()
        op[0] = int(op[0])
        if op[0] == 1:
            q.enqueue(int(op[1].strip()))
        elif op[0] == 2:
            q.pop()
        elif op[0] == 3:
            print(q.peek())
        else:
            raise Exception(f"Invalid op {op[0]}")
        #print(f"ran op: {op[0]}, stack: {q}")

main()