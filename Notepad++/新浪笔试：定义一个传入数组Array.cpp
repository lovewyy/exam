#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Array
{
private:
    int a[5];
    int n;
public:
	Array();
    Array(int t[], int n1)
	{
		for(int i = 0;i < n1; ++i)
		{
			a[i] = t[i];
		}
	}
    int num(int n);
    void fun();
    void print();
	~Array();

};

int Array::num(int n)
{
    vector<int> b;
    int result = 0;
    int r;
	int value = n;
    while(value)
    {
		r = value % 10;
        b.push_back(r);
        value = int(value / 10);
    }
    int s = b.size();
    int t = 1;
    for(int i = 0; i < s - 1; ++i)
    {
        result += t * b[i];
        t *= 10;
    }
    return result;
}

void Array::fun()
{
    int temp;
    for(int i = 0; i < 5; ++i)
    {
        for(int j = i; j < 5; ++j)
        {
            if(Array::num(Array::a[i]) > Array::num(Array::a[j]))
            {
                temp = Array::a[i];
                Array::a[i] = Array::a[j];
                Array::a[j] = temp;
            }
        }
    }
}

void Array::print()
{
    for(auto i : Array::a)
    {
        cout << i << "|";
    }
    cout << endl;
}

Array::~Array()
{
	cout << "~Array" << endl;
}

int main()
{
    int t[5] = {134, 445, 423, 233, 811};
    Array test(t, 5);
	test.fun();
    test.print();
    // cout << "811|423|233|134|445|" << endl;
    return 0;
}