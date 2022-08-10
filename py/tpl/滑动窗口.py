#!/usr/bin/env python
"""
作者：halfrost
链接：https://leetcode.cn/leetbook/read/leetcode-cookbook/56expd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
Sliding Window

双指针滑动窗口的经典写法。右指针不断往右移，移动到不能往右移动为止(具体条件根据题目而定)。
当右指针到最右边以后，开始挪动左指针，释放窗口左边界。
第 3 题，第 76 题，第 209 题，第 424 题，第 438 题，第 567 题，第 713 题，
第 763 题，第 845 题，第 881 题，第 904 题，第 978 题，第 992 题，
第 1004 题，第 1040 题，第 1052 题。


left, right = 0, 0

while right < len(s):
    // 增大窗口
    window.append(s[right])
    right ++
    while wind needs shrink:
        // 缩小窗口
        window.remove(s[left])
        left++

复杂度: O(N)
"""


# 滑动窗口算法框架
def slidingWindow(s: str, t: str):

    left, right = 0, 0
    window = list()
    while right < len(s):
        # c是待加入到窗口的字符
        c = s[left]
        # 移动指针
        right += 1
        # todo: 更新窗口数据
        window.append(c)
        print("window:{} [{}:{}]".format(window, left, right))

        #  todo: 判断左侧窗口是否要收缩, 注意条件
        while window:
            # d是将移出的字符
            d = s[left]
            # 左移窗口
            left += 1
            # todo: 更新窗口内数据
            window.remove(d)
    return


def main():
    pass


if __name__ == '__main__':
    main()
