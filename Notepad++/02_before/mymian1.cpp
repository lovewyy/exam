#include <iostream>
#include <vector>
#include <string>
#include <array>

using namespace std;

int mCutRodAux(int p[], int n, int *r);

int mCutRod(int p[], int n)
{
	int *r = new int[n+1];
	for(int i = 0; i <= n; ++i){
		r[i] = -1;
	}
	return mCutRodAux(p, n, r);
}

int mCutRodAux(int p[], int n, int *r)
{	
	if(r[n] >= 0)
	{
		return r[n];
	}
	
	int q = 0;
	if(n == 0)
	{
		q = 0;
	}
	else 
	{
		for(int i = 1; i <= n; ++i)
		{
			q = max(q, p[i - 1] + mCutRodAux(p, n - i, r));
		}
	}
	r[n] = q;
	return q;
}

int bCutRod(int p[], int n)
{
	int *r = new int[n+1];
	r[0] = 0;
	for(int j = 1; j <= n; ++j)
	{
		int q = -1;
		for(int i = 1; i <= j; ++i)
		{
			q = max(q, p[i - 1] + r[j - i]);
		}
		r[j] = q;
	}
	return r[n];
}

int main()
{   
	int p[] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 30, 30, 30};
	
	int res, res2;
	for(int i = 0; i <= 13; ++i)
	{
		res = mCutRod(p, i);
		res2 = bCutRod(p, i);
		cout << res << " ";
		cout << res2 << endl;
	}
	return 0;
}