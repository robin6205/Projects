//DO NOT MODIFY THIS FILE

#ifndef PART_H
#define PART_H

typedef struct ListNode
{
	struct ListNode * next;
	int value;
} Node;


Node * CreateNode(int val);
void LinkedListCreate(Node * * source, int len, int* arr);
void LinkedListPrint(Node * * source);
void Divide(Node** source);
void SpiltList(Node* source, Node** head1, Node** head2);

#endif
