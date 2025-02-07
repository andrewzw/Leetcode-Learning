# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import sys


def process_queries():
    queue = []
    queries = ["10\n1 76\n1 33\n2\n1 23\n1 97\n1 21\n3\n3\n1 74\n3\n"]
    for query in queries:
        cleaned = query.strip()
        queries.append(cleaned)

    n = int(queries[0])
    for i in range(1, n):
        curr_q = queries[i][0].strip()
        element = queries[i][1:].strip()

        if curr_q == "1":
            queue.append(element)
        elif curr_q == "2":
            queue.pop(0)
        elif curr_q == "3":
            print(queue[0])


process_queries()
# print(queue)

queue = []
queue.append(76)  # 1
queue.append(33)  # 1
queue.pop(0)  # 2
queue.append(23)  # 1
queue.append(97)  # 1
queue.append(21)  # 1
print(queue[0])  # 3
print(queue[0])  # 3
queue.append(74)  # 1
print(queue[0])  # 3

print(queue)


# easier
n = int(input())

queue = []
for i in range(n):
    q = input().split(" ")
    query = int(q[0])

    if query == "1":
        queue.append(q[1])
    elif query == "2":
        queue.pop(0)
    elif query == "3":
        print(queue[0])


class TwoStacksQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:  # if stack2 is empty
            while self.stack1:  # while stack1 is not empty
                removing = self.stack1.pop()  # remove each elements of stack1
                self.stack2.append(removing)  # add the removed element to end of stack2
        self.stack2.pop()  # remove the last element of stack2 after transferring all elements from stack1

    def printqueue(self):
        if self.stack2:
            print(self.stack2[-1])
        else:
            print(self.stack1[0])


if __name__ == "__main__":
    queue = TwoStacksQueue()
    n = int(input())
    for _ in range(n):
        query = input().strip().split()
        command = int(query[0])
        if command == 1:
            queue.enqueue(int(query[1]))
        elif command == 2:
            queue.dequeue()
        elif command == 3:
            queue.printqueue()
