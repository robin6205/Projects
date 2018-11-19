#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hw14.h"


#ifdef LINKEDLIST

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


// Modify the following function
#ifdef TEST_MAIN

int main(int argc, char **argv)
{
	if(argc != 2){
		return EXIT_FAILURE;
	}// if argc is less than 2 then, return EXIT_FAILURE
	// input file is specified through the Makefile.

	FILE * fptr;
	fptr = fopen(argv[1], "r");// open file to read
	if(fptr == NULL){
		printf("Error opening input file");
		return EXIT_FAILURE;// check for fopen fail. If so, return EXIT_FAILURE
	}
	int val;
	int L = 0;
	while(fscanf(fptr, "%d", &val) == 1)
	{
		L++;
	}

	int * arr = malloc(sizeof(int)*L);

	if (arr == NULL){
		fprintf(stderr, "malloc fail\n");
		fclose(fptr);
		return EXIT_FAILURE;
	}
	fseek(fptr, 0, SEEK_SET);

	int ind=0;
	while(ind < L){
		if(fscanf(fptr, "%d", &arr[ind]) != 1)
		{
			fprintf(stderr,"fscanf fail\n");
			fclose(fptr);
			free(arr);
			return EXIT_FAILURE;
		}
		ind++;
	}

	Node * head = NULL;
	LinkedListCreate(&head, L, arr);
	MergeSort(&head);
	LinkedListPrint(&head);

	fclose(fptr);
	free(arr);
//	int i = 0;
	while(head!=NULL){
		Node * temp = head;
		head = head ->next;
		free(temp);

		}


	return EXIT_SUCCESS;
}

#endif
