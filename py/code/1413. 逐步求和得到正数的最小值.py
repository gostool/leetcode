#!/usr/bin/env python
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        x = min(nums)
        left = 1
        right = abs(x * len(nums)) + 1
        while left <= right:
            mid = left + int((right - left) / 2)
            print("[{}:{}] mid:{}".format(left, right, mid))
            if self.valid(mid, nums):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def valid(self, target, nums):
        print("target:", target)
        for n in nums:
            target += n
            if target < 1:
                return False
        return True


def main():
    nums = [-3, 2, -3, 4, 2]
    ret = Solution().minStartValue(nums)
    assert 5 == ret, "ret {}".format(ret)


if __name__ == '__main__':
    main()
