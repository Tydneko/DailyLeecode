func groupAnagrams(strs []string) [][]string {
    mp := map[string][]string {}
    for _, v := range(strs){
        key := []byte(v)
        sort.Slice(key, func(i, j int)bool{ return key[i] < key[j]})
        sortedKey := string(key)
        mp[sortedKey] = append(mp[sortedKey], v)
    }

    ans := make([][]string, 0, len(mp))
    for _, v := range mp{
        ans = append(ans, v)
    }
    return ans
}