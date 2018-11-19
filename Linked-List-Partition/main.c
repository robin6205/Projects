/****************** Modify this file at specified place *************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "part.h"

/****************** DO NOT Modify this file above this line *************************/

// Modify the following function
#ifdef TEST_MAIN

int main(int argc, char **argv)
{
	if(argc != 2){
		return EXIT_FAILURE;
	}// if argc is less than 2 then, return EXIT_FAILURE
	// input file is specified through the Makefile.

	FILE * fptr;
	fptr = fopen(argv[1], "r");
	if(fptr == NULL){
		printf("Error opening input file");
		return EXIT_FAILURE;
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

	fclose(fptr);// open file to read

	// check for fopen fail. If so, return EXIT_FAILURE

	// count the number of integers in the file.

	// allocate memory to store the numbers

	// check for malloc fail, if so, return EXIT_FAILURE

// use fscanf to read the file, and store its contents into an array.

	//Node * headnode = CreateNode(arr[0]);// create head node to store the head of the linked list.
	Node * head = NULL;
	head = CreateNode(arr[0]);
	LinkedListCreate(&head, ind, arr);// call the appropriate function to create the rest of the linked list, with the values of the array.

	Divide(&head);// Divide is a function to break the lists into smaller sublists.
		// You are supposed to find the mid-point of the list, and then break the list into two lists.
		// Then the sub-lists are broken down further into smaller sub-lists.
		// Refer to the example in the README

	// Tip: check for memory errors.
	free(head);
	free(arr);
	return EXIT_SUCCESS;
}

#endif
