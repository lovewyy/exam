#include "node.h"
#include <stdio.h>
#include <stdlib.h>

// typedef struct _node{
	// int value;
	// struct _node *next;	
// }Node;

typedef struct _list{
	Node* head;
}List;

int main(){
	int number;
	List list;
	list.head = NULL;
	do
	{ 
		scanf("%d", &number);
		
		if(number != -1){
			add(&list, number);
		}
		
	}while(number != -1);
		
	return 0;
}

void add(List* pList, int number){
	Node* p = (Node*)malloc(sizeof(Node));
	p->value = number;
	p->next = NULL;

	// find the last
	Node* last = pList->head;
	if(last){
		while(last->next != NULL){
			last = last->next;
		}
		last->next = p;
	}else{
		pList->head = p;
	}
}