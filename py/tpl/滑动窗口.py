#!/usr/bin/env python
"""
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
