package code

import (
	"sort"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	nums := append([]int{}, nums1...)
	nums = append(nums, nums2...)
	sort.Ints(nums)
	//fmt.Println(nums)
	n := len(nums)
	if n%2 == 0 {
		idx := n / 2
		return float64(nums[idx-1]+nums[idx]) / 2

	} else {
		idx := n / 2
		return float64(nums[idx])
	}
}
