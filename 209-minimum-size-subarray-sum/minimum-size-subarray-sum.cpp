class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left=0;
    int right=0;
    int s=0;
    int ans=INT_MAX;
    for(right=0;right<nums.size();right++)
    {
        s=s+nums[right];
        while(s>=target)
        {
            ans=min(ans,right-left+1);
            s=s-nums[left];
            left++;
        }
    }
    if (ans==INT_MAX)
    {
        return 0;
    }
    else
    {
        return ans;
    }
    }
};