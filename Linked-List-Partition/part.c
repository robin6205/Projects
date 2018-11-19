/****************** Modify this file at specified place *************************/
#include <stdio.h>
#include <stdlib.h>
#include "part.h"

#ifdef LINKEDLIST
// Do not modify this function, we are using this within ifdef block for
// ease of grading.
void LinkedListPrint(Node * * source)
{

	Node *temp = * source;

	while(temp!=NULL)
	{
		if(temp->next!=NULL)
		{
			printf("%d,",temp->value);
		}
		else
		{
			printf("%d",temp->value);
		}
		temp=temp->next;
	}
	printf("\n");
}
#endif


/********** Do Not modify the file above this line, you can modify below ***********/
#ifdef TEST_CREATENODE

Node * CreateNode(int val)
//val: value of the element of the node to be created
{
	Node * new_node;
	new_node = malloc(sizeof(Node));
	new_node->next = NULL;
	new_node->value = val;
	// Define a new variable of type Node
	// Initialize "next", and "value" appropriately

	return new_node;//return the newNode
}
#endif

#ifdef TEST_LINKEDLISTCREATE
//head: the head of the singly linkedlist.
//len: the length of the array.
//arr: the array with the contents of the input file.

//This function will create and initialize the singly linkedlist with length=len,

void LinkedListCreate(Node * * source, int len, int* arr)
{
	int i;

	Node * t = *source;
	for(i = 1; i<len;i++){
		Node * p = CreateNode(arr[i]);
		t -> next = p;
		t = t->next;
	}
	free(t);

	// This function is similar to the one in HW12.
	// Tip: use CreateNode(arr[index])
}
#endif


#ifdef TEST_SPLIT
// source is the Node corresponding to the head of the list
// head1 is the list corresponding upper half of the list. (After Partition)
// head2 is the list corresponding lower half of the list. (After Partition)
void SpiltList(Node* source, Node** head1, Node** head2)
{
	  int mid;// Find the mid point of the list.
		int num = 0;
		Node * p = source;

	while(p!=NULL)
	{
		p =p->next;
		num++;
	}

		if(num%2==0){
			mid = num/2;
		}//in case of an even number of nodes, mid point will be floor(<num_elements>/2)
			//Example: 1,2,3,4
				// The list should split into 1,2 and 3,4

		else{
			mid = (num/2)+1;
		}//in case of an odd number of nodes, mid point will be <num_elements>/2
			//Example: 1,2,3,4,5
			// The list should split into 1,2,3 and 4,5

	*head1=source;	// Tip: head1 will point to the source node.
	p = *head1;
	int cnt =1;
	while(cnt != mid){
		p = p -> next;
		cnt++;
	}
	*head2=p->next; // Tip: head2 will point to the mid-point of the list.
	p->next = NULL;
	// Tip: Ensure you break the link between the sub-lists.
}
#endif


#ifdef TEST_DIV
void Divide(Node** source)
{
	Node * headnode1 ;// Declare a node, to hold the current head of source list.
	Node * headnode2 ;
	Node * nd = *source;
	// Declare nodes, to hold the two the heads of the two sub-lists.
	if(source == NULL){
		return;
	}
	if(nd->next == NULL){
		return;
	}
	/*if(length == 0 || length == 1){
		return;
	}*/
	// Check for the base case -- length 0 or 1
		// if so, return;

	SpiltList(*source, &headnode1, &headnode2);// Use SpiltList(...) to partition the list into sub lists.

	LinkedListPrint(&headnode1);// Use LinkedListPrint(...); to print the upper sub-list.
	LinkedListPrint(&headnode2);// Use LinkedListPrint(...); to print the lower sub-list
		// DO NOT USE YOUR OWN PRINT FUNCTION.

	 Divide(&headnode1);// Recursively Divide(...) both sub-lists, to find their respective mid-points
	 Divide(&headnode2);// till only one or no elements are left in the sub-lists.
}
#endif
