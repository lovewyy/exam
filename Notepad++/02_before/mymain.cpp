#include <iostream>
#include <vector>
#include <string>
#include <array>

using namespace std;

//he bing
void sortArray(int a[], int first, int mid, int last, int temp[])
{
	int i = first, j = mid + 1;
	int m = mid, n = last;
	int k = 0;
	
	while(i <= m && j <= n)
	{
		if(a[i]<=a[j])
		{			
			temp[k++] = a[i++];
		}
		else
		{
			temp[k++] = a[j++];
		}
	}
	
	while(i <= m)
	{
		temp[k++] = a[i++];
	}
	
	while(j <= n)
	{
		temp[k++] = a[j++];
	}
	
	for(i = 0;i < k; i++)
	{
		a[first + i] = temp[i];
	}
}

void mergeSort(int a[], int first, int last, int temp[])
{
	if(first < last)
	{
		int mid = (first + last) / 2;
		mergeSort(a, first, mid, temp);
		mergeSort(a, mid + 1, last, temp);
		sortArray(a, first, mid, last, temp);
	}
}

bool MergeSort(int a[], int n)
{
	int *p = new int[n];
	mergeSort(a, 0, n - 1, p);
	delete[] p;
	return true;
}

int main(){
	int a[] = {1, 3, 5, 2, 4, 6, 1, 3, 5, 2, 4, 2, 2, 5};
	int n = sizeof(a) / sizeof(a[0]);
	bool t = MergeSort(a, n);
	cout<< t<< endl;
	for(int i = 0; i != n; ++i)
	{
		cout << a[i] << " ";
	}
	cout<< endl;
	return 0;
}