package code

import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for k, v := range nums {
		if idx, ok := m[target-v]; ok {
			return []int{idx, k}
		}
		m[v] = k
	}
	return nil
}

func twoSumList(ansMap map[string]bool, nums []int, target int) []int {
	m := make(map[int]bool)
	ans := make([][]int, 0)
	for _, a := range nums {
		b := target - a
		if _, ok := m[b]; ok {
			k := fmt.Sprintf("%v+%v=%v", a, b, target)
			fmt.Printf("%v+%v=%v", a, b, target)

			ans = append(ans, []int{a, b})
		}
		m[a] = true
	}
	return nil
}
