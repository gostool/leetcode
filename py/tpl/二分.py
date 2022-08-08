#!/usr/bin/env python
from typing import List


# 标准二分
def binary_search(nums: List[int], target: int) -> int:
    # 1.[l, r] 闭区间
    left, right = 0, len(nums)-1
    # 2.判断 <=; 循环结束的条件是 left>right, [right+1, right]
    while left <= right:
        # 3. 计算mid
        mid = int(left + (right-left)/2)
        if nums[mid] == target:
            return mid
        # 小于target, [mid+1:right]
        elif nums[mid] < target:
            left = mid + 1
        # 大于target, [left:mid-1]
        elif nums[mid] > target:
            right = mid - 1
    return -1


# 最左侧二分
def left_binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # 在[left, mid-1],
    #   如果无解，循环终止条件: left=mid
    #   如果有解, [left, mid-1] 中找到新的mid
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    if left < len(nums) and nums[left] != target:
        return -1
    return left


def right_binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # 在[left, mid-1],
    #   如果无解，循环终止条件: left=mid
    #   如果有解, [left, mid-1] 中找到新的mid
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    if right < len(nums) and nums[right] != target:
        return -1
    return right


def main():
    nums = [1, 2, 3, 4, 5]
    assert 1 == binary_search(nums, 2)

    nums_left = [1, 2, 2, 2, 3, 4, 5]
    ret = left_binary_search(nums_left, 2)
    assert ret == 1, "left ret:{}".format(ret)

    nums_left = [0, 1, 2, 2, 3, 4]
    ret = right_binary_search(nums_left, 2)
    assert ret == 3, "right ret:{}".format(ret)


if __name__ == '__main__':
    main()
