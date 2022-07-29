#!/usr/bin/env python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = dict()
        for idx, v in enumerate(nums):
            other = target - v
            if other in idx_map:
                return [idx_map[other], idx]
            idx_map[v] = idx
        return


def main():
    pass


if __name__ == '__main__':
    main()
