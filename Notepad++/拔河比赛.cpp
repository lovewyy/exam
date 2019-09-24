#include<iostream>
#include<cstdio>
using namespace std;
int n,a[1001],t,s,f[1001][1001];
int main()
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
	   scanf("%d",&a[i]);
	   s+=a[i];//求总重量
	}
	
	t=s/2;
	f[0][0]=1; 
	
	  for(int i=1;i<=n;i++)
	  {
		for(int j = min(n/2,i-1);j>=0;j--)
		{
		   for(int k=0;k <= j * 450;k++)//因为每个人不可能超过450
			{
				if(f[j][k]) f[j+1][k+a[i]]=1;//前j个有k个是可以的
			}
		}
	  }
	  
	  for(int i=0;1;i++)
	  {
	  	if(f[n/2][t+i])
	  	{//第一队和第二队
	  	    printf("%d %d",min(t+i,s-t-i),max(t+i,s-t-i));//输出最大最小
	  		break;
	  	}
	  	if(f[n/2][t-i])
	  	{//第一队和第二队
	  		printf("%d %d",min(t+i,s-t+i),max(t+i,s-t+i));//输出最大最小
	  		break;
	  	}
	  }
	return 0;
}