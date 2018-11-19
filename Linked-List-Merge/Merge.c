#include <stdio.h>
#include <stdlib.h>
#include "main.h"


#ifdef TEST_CREATENODE

Node * CreateNode(int val)
//val: value of the element of the node to be created
{
  Node * new_node;
  new_node = malloc(sizeof(Node));
  new_node->next = NULL;
  new_node->value = val;

  return new_node;
	// same as previous homeworks
}
#endif

#ifdef TEST_LINKEDLISTCREATE
//source: the head of the singly linkedlist.
//len: the length of the array.
//arr: the array with the contents of the input file.

void LinkedListCreate(Node * * source, int len, int* arr)
{
  int i;
  *source = CreateNode(arr[0]);
  Node * t = *source;
  for(i = 1; i<len;i++){
    Node * p = CreateNode(arr[i]);
    t -> next = p;
    t = t->next;
  }
  free(t);
	// Refer HW13 and HW12
	// Tip: use CreateNode(arr[index])
}
#endif


#ifdef TEST_SPLIT
// source is the head of the list to be split.
// head1 is the head of the upper sub-list.
// head2 is the head of the lower sub-list.

void SplitList(Node* source, Node** head1, Node** head2)
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
	// Refer HW13
}
#endif

#ifdef TEST_MERGE
// upper is the upper sub-list to be merged
// lower is the lower sub-list to be merged
Node* Merge(Node* upper, Node* lower)
{
  Node * temp;

  if(upper == NULL){
    return(lower);
  }
  if(lower == NULL){
    return(upper);
  }

  if((upper -> value) < (lower->value)){
    temp = upper;
    temp -> next = Merge(upper ->next, lower);
  }
  else{
    temp = lower;
    temp ->  next = Merge(upper, lower->next);
  }
	// Check for the base cases. (When either sub-list is NULL)

	// Pick the larger between upper and lower, and recur appropriately.

	return temp;// return the merged array
}
#endif

#ifdef TEST_SORT
// source is the head of the list to for which MergeSort is to be performed.
void MergeSort(Node** source)
{
  Node * upper;
  Node * lower;
	// Declare a node, to hold the current head of the source list.

// Declare nodes, to hold the two the heads of the two sub-lists.
  if((*source) -> next == NULL){
    return;
  }
  if(*source == NULL){
    return;
  }
	// Check for the base case -- length 0 or 1
		// if so, return;

	SplitList((*source), &upper, &lower);// Use SpiltList() to partition the list into sub lists.
		// This will partiton the source list, into two lists (As done in the previous homework)

	MergeSort(&upper);// Recursively sort the sub-lists by calling MergeSort() on the upper and lower sub-lists.
		MergeSort(&lower);// MergeSort() is a recursive function, and MergeSort() needs to be called
		// on both sub-lists (obtained after partitioning)

	*source = Merge(upper, lower);// Merge the two sorted lists together, using the Merge()
}
#endif
