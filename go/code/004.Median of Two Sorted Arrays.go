package code

func merge(nums1 []int, nums2 []int) (nums []int) {
	low1, low2 := 0, 0
	for low1 < len(nums1) && low2 < len(nums2) {
		if nums1[low1] < nums2[low2] {
			nums = append(nums, nums1[low1])
			low1++
		} else {
			nums = append(nums, nums2[low2])
			low2++
		}
	}
	if low1 >= len(nums1) {
		nums = append(nums, nums2[low2:]...)
	}
	if low2 >= len(nums2) {
		nums = append(nums, nums1[low1:]...)
	}
	return
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	//nums := append([]int{}, nums1...)
	//nums = append(nums, nums2...)
	//sort.Ints(nums)
	nums := merge(nums1, nums2)
	//fmt.Println(nums)
	n := len(nums)
	if n%2 == 0 {
		return float64(nums[n/2]+nums[(n/2-1)]) / 2
	}
	return float64(nums[n/2])
}
