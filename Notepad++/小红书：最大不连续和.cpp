#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<algorithm>
#include<cstdlib>
using namespace std;
const int maxn = 1010;
const int INF = 0x3f3f3f3f;
int value[maxn];
int dp[maxn][maxn][2];
int Max(int a,int b,int c){
    int t = max(a,b);
    return max(t,c);
}
int main()
{
    //freopen("in.txt","r",stdin);
    ios::sync_with_stdio(false);
    int n;
    cin>>n;
    for(int i=1;i<=n;++i)
        cin>>value[i];
    memset(dp,0,sizeof(dp));
    dp[1][1][1] = value[1];
    for(int i=2;i<=n;++i){
        dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][1][1]);
        dp[i][1][1] = max(dp[i-1][0][0],dp[i-2][0][0]) + value[i];
    }
    for(int i=2;i<=n;++i){
        for(int j=2;j<=(i+1)/2;++j){
            dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]);
            dp[i][j][1] = Max(dp[i-1][j-1][0],dp[i-2][j-1][1],dp[i-2][j-1][0]) + value[i];
        }
    }
    int ans,have=0;
    for(int i=(n+1)/2;i>=0;--i){
        for(int j=0;j<2;++j){
            if(dp[n][i][j] >= have){
                ans = i;
                have = dp[n][i][j];
            }
        }
    }
    cout<<have<<" "<<ans<<endl;
    return 0;
}