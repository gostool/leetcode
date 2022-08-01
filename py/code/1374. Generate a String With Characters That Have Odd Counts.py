#!/usr/bin/env python
from typing import List


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return "a" + "b"*(n-1)
        return "a" * n


def main():
    pass


if __name__ == '__main__':
    main()
