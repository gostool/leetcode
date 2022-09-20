package code

import (
	"sort"
)

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	dp[0] = 0
	sort.Ints(coins)
	for i := 1; i < amount+1; i++ {
		n := amount + 1
		dp[i] = n
		for _, coin := range coins {
			if coin > i {
				break
			}
			n = min(n, 1+dp[i-coin])
		}
		dp[i] = n
	}
	if dp[amount] == (amount + 1) {
		return -1
	}
	return dp[amount]
}
