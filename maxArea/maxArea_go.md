func maxArea(height []int) int {
    left, right := 0, len(height)-1
    ans := 0
    for left < right{
        val := (right-left)*(min(height[right], height[left]))
        ans = max(ans, val)
        if height[left] <= height[right]{
            left++
        }else{
            right--
        }
    }
    return ans
}