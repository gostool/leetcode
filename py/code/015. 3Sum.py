#!/usr/bin/env python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        使用双指针计算两数和

        :param nums: 有序的待扫描数组
        :param target: 目标值
        :return: 所有的解, 不重复
        """
        left, right = 0, len(nums)-1
        ans = list()
        while left < right:
            t = nums[left] + nums[right]
            if target == t:
                ans.append([nums[left], nums[right], -target])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif t > target:
                right -= 1
            else:
                left += 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return list()
        nums.sort()
        print(nums)
        ans = list()
        for i in range(0, len(nums)-2):
            target = nums[i]
            if target > 0:
                continue
            if i >= 1 and target == nums[i-1]:
                continue
            ret = self.twoSum(nums[i+1:], -target)
            # print(target, ret)
            ans.extend(ret)
        return ans


def main():
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0, 0]
    ret = s.threeSum(nums)
    print(ret)


if __name__ == '__main__':
    main()
