#!/usr/bin/env python

from queue import PriorityQueue


def main():

    q = PriorityQueue()
    q.put((2, 'code'))
    q.put((1, 'eat'))
    q.put((3, 'sleep'))
    while not q.empty():
        next_item = q.get()
        print(next_item)


if __name__ == '__main__':
    main()
