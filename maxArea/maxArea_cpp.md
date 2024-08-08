class Solution {
public:
    int maxArea(vector<int>& height) {
        int area = 0;
        int x = 0, y = 0;
        int l = 0, r = height.size() - 1;
        while(l < r){
            x = r - l;
            y = min(height[l], height[r]);
            area = max(area, x*y);
            height[l] <= height[r] ? ++l: --r;
        }
        return area;
    }
};