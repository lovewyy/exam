#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& , int, int);

void quickSort(vector<int>& a, int f, int l)
{
	int m;
	if( f < l)
	{
		m = partition(a, f, l);
		quickSort(a, f, m-1);
		quickSort(a, m+1, l);
	}
}

int partition(vector<int>& a, int f, int l)
{
	int key = a[l];
	int i = f - 1;
	int temp;
	for(int j = f; j < l; j++)
	{
		if(key >= a[j])
		{
			i += 1;
			temp = a[j];
			a[j] = a[i];
			a[i] = temp;
		}
	}
	temp = a[i+1];
	a[i+1] = a[l];
	a[l] = temp;
	
	return i+1;
}


int main()
{
	vector<int> a = {1, 2, 0, 3, 2, 1, 4, 5, 3, 8, 1};
	quickSort(a, 0, 10);
	for(int i = 0; i < 11; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
	return 0;
}