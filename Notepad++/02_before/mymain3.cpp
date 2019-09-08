#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
const int N=105,MOD=1000007;
int n,m,a[N];
int f[N][N];
int main(int argc, const char * argv[]) {
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++) scanf("%d",&a[i]),f[i][0]=1;
    for(int i=0;i<=a[1];i++) f[1][i]=1;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++){
            for(int k=j-a[i];k<=j;k++)
                if(k>=0)f[i][j]=(f[i][j]+f[i-1][k])%MOD;
        }
    printf("%d",f[n][m]);
    return 0;
}