//https://leetcode.com/problems/sliding-window-maximum/submissions/1096166572/
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> results;
        deque<int> container;
        for (int i = 0; i < nums.size(); i++) {
            while (!container.empty() && container.front()<i-k+1){
                container.pop_front();
            }
            while (!container.empty() && nums[container.back()]<nums[i]){
                container.pop_back();
            }
            container.push_back(i);
            if (i>=k-1) {
                results.push_back(nums[container.front()]);
            }
        }
        return results;
    }
};