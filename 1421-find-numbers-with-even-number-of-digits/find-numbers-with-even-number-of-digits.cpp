class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        
        for(int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int cd = 0;
            
            while(num > 0) {
                cd++;
                num /= 10;
            }
            
            if(cd % 2 == 0) {
                count++;
            }
        }
        
        return count;
    }
};
