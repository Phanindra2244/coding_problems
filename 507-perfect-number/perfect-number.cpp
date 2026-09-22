class Solution {
public:
    bool checkPerfectNumber(int num) {
        vector<int>t;
        int c=0;
	    for(int i=1;i<num;i++)
        {
            if(num%i==0)
            {
                t.push_back(i);
            }
        }
        for(int j=0;j<t.size();j++)
        {
            c=c+t[j];
        }
        if (c==num)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};