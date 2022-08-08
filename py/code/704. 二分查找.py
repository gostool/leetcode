#!/usr/bin/env python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        # [left, right]
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + int((right-left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    ret = Solution().search(nums, target)
    assert ret == 4, "ret {}".format(ret)
    pass


if __name__ == '__main__':
    main()
