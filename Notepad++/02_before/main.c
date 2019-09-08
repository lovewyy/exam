#include "array.h"
#include <stdio.h>

// typedef struct{
	// int* array;
	// int size;
// }Array;

// Array array_create(int init_size);
// void array_free(Array *a);
// int array_size(const Array *a);
// int* array_at(Array *a, int index);
// void array_inflate(Array *a, int more_size);

int main()
{
	printf("hello");
	Array a = array_create(100);
	printf("%d\n", array_size(&a));
	*array_at(&a, 10) = 20;
	printf("%d\n", *array_at(&a, 10));
	
	return 0;
}