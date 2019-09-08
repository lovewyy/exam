#include <iostream>
#include <vector>
using namespace std;

int func(vector<int> test, int k, int m)
{
	int count = m;
	if(m == 0) return int(30 / (k + 1));
	vector<int> x, y, z;
	int mid;
	int v = test[0];
	while(v > 0)
	{
		if(v - k - 1 >= 1)
		{
			x.push_back(v - k - 1);
			count += 1;
		}
		v -= k + 1;
	}
	
	int back = test[m - 1];
	while(back < 30)
	{
		if(back + k + 1 <= 30)
		{
			y.push_back(back + k + 1);
			count += 1;
		}
		back += k + 1;
	}
	
	for(int i = 0; i < m - 1; ++i)
	{
		mid = test[i] + k + 1;
		while(mid + k + 1 <= test[i + 1])
		{
			z.push_back(mid + k + 1);
			count += 1;
			mid += k + 1;
		}
	}
	return count;
}

int main()
{
	int n;
	cin >> n;
	vector<int> test;
	for(int i = 0; i < n; ++i)
	{
		int k, m, d;
		cin >> k >> m;
		test.clear();
		for(int i = 0; i < m; ++i)
		{
			cin >> d;
			test.push_back(d);
		}
		cout << func(test, k, m) << endl;
	}
	return 0;
}