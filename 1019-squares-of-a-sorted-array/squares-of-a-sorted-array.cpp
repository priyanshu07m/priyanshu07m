class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        int i = 0;
        int j = n-1;
        int k  = n-1;
        while(i<=j){
            if(abs(nums[i])<abs(nums[j])){
                res[k] = abs(nums[j]) * abs(nums[j]);
                j--;
                k--;
            }
            else{
                res[k] = abs(nums[i]) * abs(nums[i]);
                i++;
                k--;

            }
        }
        return res;
        
    }
};