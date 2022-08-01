#!/usr/bin/env python
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        暴力解法
        :param height:
        :return:
        """
        ans = 0
        for i in range(len(height)-1):
            h1 = height[i]
            for j in range(i+1, len(height)):
                h2 = height[j]
                h = min(h2, h1)
                s = h * (j-i)
                # print(i+1, j+1, "x", j-i, h, s)
                ans = max(ans, s)
        return ans

    def maxAreaV2(self, height: List[int]) -> int:
        """
        双指针
        s = w * h
        s1 = (r-l)*min(h[l], h[r]), s1是最大宽度下的面积.
        随后宽度变小，只有高度更大的情况下，才可能出现面积最大

        :param height:
        :return:
        """
        ans = 0
        l, r = 0, len(height)-1
        while l < r:
            s = min(height[l], height[r]) * (r-l)
            ans = max(ans, s)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


def main():
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9]
    assert 49 == s.maxAreaV2(height)

    height = [1, 2]
    assert 1 == s.maxAreaV2(height)


if __name__ == '__main__':
    main()
