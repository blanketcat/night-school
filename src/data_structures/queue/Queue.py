#!/usr/bin/env python3

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


def main():
    pass


if __name__ == '__main__':
    main()
