#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Node
{
	int root;
	int left;
	int right;
};

int main()
{
	int n;
	cin >> n;
	vector<Node> test(n);
	int root, left, right;
	vector<int> num(n, 0);
	for(int i = 0; i < n; ++i)
	{
		cin >> test[i].root >> test[i].left >> test[i].right;
		
		if(test[i].left != -1)
		{
			num[test[i].left] = 1;
		}
		if(test[i].right != -1)
		{
			num[test[i].right] = 1;
		}
	}
	// = 0
	int froot = -1;
	for(int i = 0; i < n; ++i)
	{
		if(num[i] == 0)
		{
			froot = i;
			break;
		}
	}
	// 层次遍历
	vector<int> treeSum;
	queue<Node> q;
	q.push(test[froot]);
	while(!q.empty())
	{
		int sq = q.size();
		int cnt = 0;
		for(int i = 0; i < sq; ++i)
		{
			Node head = q.front();
			cnt += head.root;
			q.pop();
			if(head.left != -1)
			{
				q.push(test[head.left]);
			}
			if(head.right != -1)
			{
				q.push(test[head.right]);
			}
		}
		treeSum.push_back(cnt);
	}
	bool ans = true;
	int l = treeSum.size();
	for(int i = 1; i < l; ++i)
	{
		if(treeSum[i] < treeSum[i - 1])
		{
			ans = false;
			break;
		}
	}
	if(ans == false) cout << "NO" << endl;
	else cout << "YES" << endl;
	return 0;
}