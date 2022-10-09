#!/usr/bin/env python

import heapq

"""
1.堆排序 可以通过将所有值推入堆中然后每次弹出一个最小值项来实现
2.优先队列实现说明
3.nlargest(n,iter)、nsmallest(n,iter)

heapreplace(heap，n)弹出最小的元素被n替代
heappush(heap,n)数据堆入
heappop(heap)将数组堆中的最小元素弹出
"""


def test():
    q = []
    heapq.heappush(q, (2, 'code'))
    heapq.heappush(q, (1, 'eat'))
    heapq.heappush(q, (3, 'sleep'))
    while q:
        next_item = heapq.heappop(q)
        print(next_item)


def heapsort(iterable):
    """
    https://docs.python.org/zh-cn/3/library/heapq.html
    堆排序 可以通过将所有值推入堆中然后每次弹出一个最小值项来实现。

    :param iterable:
    :return:
    """
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


def top_n(n=1, iterable=None):
    return heapq.nlargest(n, iterable)


def small_n(n=1, iterable=None):
    return heapq.nsmallest(n, iterable)


def main():
    data = [1, 3, 5, 8, 2, 4]
    data = heapsort(data)
    print(data)
    print("top", top_n(2, data))
    print("small", small_n(2, data))
    test()


if __name__ == '__main__':
    main()
