package code

import "sort"

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

// twoSumList
// 使用双指针
func twoSumList(nums []int, target int) [][]int {
	sort.Ints(nums)
	ans := make([][]int, 0)
	left, right := 0, len(nums)-1
	for left < right {
		ret := nums[left] + nums[right]
		if ret == target {
			ans = append(ans, []int{nums[left], nums[right]})
			// 考虑重复元素
			for nums[left+1] == nums[left] {
				left++
			}
			for nums[right-1] == nums[right] {
				right--
			}
			left++
			right--
		} else if ret < target {
			left++
		} else {
			right--
		}
	}
	return ans
}
