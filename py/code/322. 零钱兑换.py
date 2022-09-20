#!/usr/bin/env python
from typing import List




class Solution:
    """
    给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 默认使用1
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            # 最大不能超过amount+1个数量
            n = amount+1
            for coin in coins:
                if coin > i:
                    break
                n = min(n, 1+dp[i-coin])
            dp[i] = n
        if dp[amount] == (amount+1):
            return -1
        return dp[amount]


def main():
    # coins = [1, 2, 5]
    # amount = 11
    # ret = Solution().coinChange(coins, amount)
    # assert ret == 3, "ret:{} != 3".format(ret)

    # coins = [2]
    # amount = 3
    # ret = Solution().coinChange(coins, amount)
    # assert ret == -1, "ret:{} != -1".format(ret)

    # coins = [1]
    # amount = 0
    # ret = Solution().coinChange(coins, amount)
    # assert ret == 0, "ret:{} != 0".format(ret)

    coins = [474, 83, 404, 3]
    amount = 264
    ret = Solution().coinChange(coins, amount)
    assert ret == 8, "ret:{} != 8".format(ret)


if __name__ == '__main__':
    main()
