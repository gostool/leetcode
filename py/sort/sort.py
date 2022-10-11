#!/usr/bin/env python

# 第一题
def line_sum(m=0, w=0):
    # 1.计算高度
    if m % w == 0:
        h = m//w
    else:
        h = m//w + 1

    # 2.计算下标
    i, j = 0, 0
    flag = 1
    # 3.计算求和
    ret = 0
    data = [i for i in range(1, m+1)]
    while i < h:
        idx = i*w+j
        if idx >= m:
            break
        # print(i, j, data[idx])
        ret += data[idx]
        i += 1
        j += flag
        if j > (w-1) or j < 0:
            flag *= (-1)
            j %= (w-1)
    return ret


# 第二题
def inner(j=1, data_str=""):
    data = []
    for idx in range(0, len(data_str)-j+1):
        w = data_str[idx:idx+j]
        data.append(w)
    return data


def group(data_str, n):
    ans = []
    for i in range(1, n):
        ans.extend(inner(i, data_str))
    return ans


def main():
    # m = 8
    # w = 3
    # ret = line_sum(m, w)
    # assert ret == 6, "ret:{}".format(ret)

    # m = 18
    # w = 3
    # ret = line_sum(m, w)
    # assert ret == 56, "ret:{}".format(ret)
    data = "我是中国人"
    ret = group(data, len(data)+1)
    print(ret)


if __name__ == '__main__':
    main()
