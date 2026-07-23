class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        int j = i+1;
        int k = 1;
        while(j<n){
               if(nums[j]==nums[j-1]){
            j++;
        }
        else{
             nums[i+1]=nums[j];
        i++;
        k++;
        j++;    
    }

 }
       

     return k;
        }
     
};