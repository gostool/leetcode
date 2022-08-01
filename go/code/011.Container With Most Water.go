package code

import "math"

func maxArea(height []int) int {
	ans := float64(0)
	s := float64(0)
	l, r := 0, len(height)-1

	for l < r {
		s = math.Min(float64(height[l]), float64(height[r])) * float64(r-l)
		ans = math.Max(ans, s)
		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}
	return int(ans)
}
