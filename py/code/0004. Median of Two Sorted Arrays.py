#!/usr/bin/env python
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        nums = list()
        len_n1 = len(nums1)
        len_n2 = len(nums2)
        l1 = 0
        l2 = 0
        # 归并
        while l1 < len_n1 and l2 < len_n2:
            if nums1[l1] < nums2[l2]:
                nums.append(nums1[l1])
                l1 += 1
            else:
                nums.append(nums2[l2])
                l2 += 1
            # print(nums, l, l1, l2)
        if l1 < len_n1:
            nums.extend(nums1[l1:])

        if l2 < len_n2:
            nums.extend(nums2[l2:])
        l = len(nums)
        # print(nums, l, l %2 )
        if l % 2 == 0:
            idx = l // 2
            n = nums[idx - 1] + nums[idx]
            return n / 2
        else:
            idx = l // 2
            return nums[idx]


def main():
    pass


if __name__ == '__main__':
    main()
