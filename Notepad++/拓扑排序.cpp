#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
typedef long long ll;

vector<int>edge[30010],ans;
priority_queue<int>q;
int in[30010];
int T,n,m;
void init()
{
    for(int i=1;i<=n;i++)
    {
        edge[i].clear();
        in[i]=0;
    }
    while(!q.empty()) q.pop();
    ans.clear();
}
void solve()
{
    int i,j;
    for(i=1;i<=n;i++)
        if(in[i]==0) q.push(i);
    while(!q.empty())
    {
        int p=q.top(); q.pop();
        ans.push_back(p);
        for( i=0; i<edge[p].size(); i++ )
        {
            int v=edge[p][i];
            in[v]--;
            if(in[v]==0) q.push(v);
        }
    }
    for(i=ans.size()-1;i>0;i--)
        printf("%d ",ans[i]);
    printf("%d\n",ans[0]);
}
int main()
{
    int a,b;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        init();
        while(m--)
        {
            scanf("%d%d",&a,&b);
            edge[b].push_back(a);
            in[a]++;
        }
        solve();
    }
    return 0;
}
