// pthread
#inlcude <stdio.h>
#include <pthread.h>

class Hello
{
	public static void* Say_hello(void* arg)
	{
		printf("hello from thread.\n");
		pthread_exit((void*)2);
	}
};

int main()
{
	pthread_t tid;
	int iRet =  pthread_create(&tid, NULL, Hello::Say_hello, NULL);
	void* as;
	pthread_join(tid, &as);
	printf("as=%ld\n", (long)as);
	return 0;
}