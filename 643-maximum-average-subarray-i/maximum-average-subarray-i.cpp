class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        vector <double> res;
        int left=0;
    int right=0;
    int s=0;
    for(right=0;right<nums.size();right++)
    {
        s=(s+nums[right]);
        if((right-left+1)==k)
        {
        	double b=double(s)/k;
            res.push_back(b);
            s=s-nums[left];
            left++;
        }
    }

    double x= *max_element(res.begin(),res.end());
    return x;
    }
};