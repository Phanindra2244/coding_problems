class Solution {
public:
     int rev(int k,int c)
     {
     vector <int> l;
     int d;
     while(k>0)
     {
        d=k%10;
        l.push_back(d);
        k=k/10;
     }
     if(!l.empty() && l[0]==0)
     {
        l.erase(l.begin());
     }
     long long int num=0;
     for(int i=0;i<l.size();i++)
     {
        num=num*10+l[i];
     }
     if(num< -pow(2,31)||num>pow(2,31)-1)
        {
            return 0;
        }
     if(c>0)
     {
        return num*-1;
     }
     else
     {
        return num;
     }
    }
public:
    int reverse(int x) {
        long long k;
        k=x;
        int c=0;
        if(k<0)
        {
           k=abs(k);
           c++;
        }
        int ans=rev(k,c);
        return ans;
    }
};