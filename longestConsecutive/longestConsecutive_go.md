func longestConsecutive(nums []int) int {
    numSet := map[int]bool{}
    for _, num := range nums{
        numSet[num] = true
    }

    longestStreak := 0
    for num := range numSet{
        if !numSet[num-1]{
            currentNum, currentStreak := num, 1

            for numSet[currentNum+1]{
                currentStreak++
                currentNum++
            }

            if currentStreak > longestStreak{
                longestStreak = currentStreak
            }
        }
    }
    return longestStreak
}