package code

// lengthOfLongestSubstring O(N)
func lengthOfLongestSubstring(s string) int {
	left, right := 0, 0
	ans := 0
	inValid := false
	window := map[string]int{}
	for right < len(s) {
		// 增加窗口
		c := string(s[right])
		right++
		window[c]++
		if window[c] > 1 {
			inValid = true
		}

		// 是否收缩窗口
		for inValid {
			d := string(s[left])
			left++
			window[d]--
			if window[c] <= 1 {
				inValid = false
			}
		}
		ans = max(ans, right-left)
	}

	return ans
}

// btLengthOfLongestSubstring 暴力计算 O(N2)
func btLengthOfLongestSubstring(s string) int {
	n := len(s)
	ans := 0
	// 固定起点，向后遍历，找到重复的退出
	for i := 0; i < n; i++ {
		set := map[string]bool{}
		set[string(s[i])] = true
		j := i + 1
		for ; j < n; j++ {
			c := string(s[j])
			if _, ok := set[c]; ok {
				break
			}
			set[c] = true
		}
		ans = max(ans, j-i)
	}
	return ans
}
