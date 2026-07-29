class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        int i = 1;
        sort(nums.begin(),nums.end());
        while(i<n){
            if(nums[i]==nums[i-1]){
                return true;
            }
            i++;
        }
        return false;

        
    }
};