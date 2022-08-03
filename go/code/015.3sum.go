package code

import (
	"fmt"
	"sort"
)

// [0, 1, 2, 3, 4] 5 2
func threeSum(nums []int) [][]int {
	if len(nums) < 3 {
		return [][]int{}
	}
	sort.Ints(nums)
	var ans [][]int
	for i := 0; i < len(nums)-2; i++ {
		target := nums[i]
		// 处理重复元素
		if i >= 1 && target == nums[i-1] {
			continue
		}
		// 不存在三个正数相加 > 0
		if target > 0 {
			continue
		}
		fmt.Printf("i:%v nums:%v target:%v\n", i, nums, target)
		// 计算: 在数组中存在加和为-target
		left := i + 1
		right := len(nums) - 1
		for left < right {
			ret := target + nums[left] + nums[right]
			if ret == 0 {
				// 成功找到, 加入结果集合
				ans = append(ans, []int{target, nums[left], nums[right]})
				fmt.Printf("ans:%v left:%v right:%v\n", ans, left, right)
				// 同时移动左右指针
				left++
				right--
				// 考虑 去重
				for left < right && nums[left] == nums[left-1] {
					left++
				}
				for left < right && nums[right] == nums[right+1] {
					right--
				}
			} else if ret > 0 {
				// 过大
				right--
			} else {
				// 过小
				left++
			}
		}
	}
	return ans
}
