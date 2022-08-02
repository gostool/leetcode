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

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        """
        使用双指针优化
        :param nums:
        :param target:
        :return:
        """
        nums.sort()
        left, right = 0, len(nums)-1
        ans = list()
        while left < right:
            t = nums[left] + nums[right]
            if target == t:
                ans.append([nums[left], nums[right]])
                while nums[left] == nums[left+1]:
                    left += 1
                while nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif t > target:
                right -= 1
            else:
                left += 1
        return ans


def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution().twoSumV2(nums, target)
    print(s)
    pass
    assert s == [[2, 7]]


if __name__ == '__main__':
    main()
