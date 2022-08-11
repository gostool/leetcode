#!/usr/bin/env python
# from typing import DefaultDict, Counter
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
        :param s:
        :return:
        """
        left, right = 0, 0
        window = Counter("")
        valid = True
        ans = 0
        while right < len(s):
            # 增加窗口
            c = s[right]
            right += 1
            window[c] += 1
            # 判断满足匹配要求
            if window[c] > 1:
                valid = False

            # 判断是否收缩
            while not valid:
                # 左边移除d, 判断c的数量是否满足要求
                d = s[left]
                left += 1
                window[d] -= 1
                if window[c] <= 1:
                    valid = True
            # 获取最长子串
            ans = max(ans, right-left)
            # if right-left >= ans:
            #     print("update", s[left:right])
            #     ans = right-left
        return ans


def main():
    s = "abcdec"
    ret = Solution().lengthOfLongestSubstring(s)
    assert 5 == ret, "s:{} ret {}".format(s, ret)
    #
    # s = "abcabcbb"
    # ret = Solution().lengthOfLongestSubstring(s)
    # assert 3 == ret, "s:{} ret {}".format(s, ret)
    #
    # s = "pwwkew"
    # ret = Solution().lengthOfLongestSubstring(s)
    # assert 3 == ret, "s:{} ret {}".format(s, ret)
    #
    # s = "bbb"
    # ret = Solution().lengthOfLongestSubstring(s)
    # assert 1 == ret, "s:{} ret {}".format(s, ret)


if __name__ == '__main__':
    main()
