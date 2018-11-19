#include "hw10.h"
//modify the main() function
#ifdef TEST_MAINFUNC

int main(int argc, char **argv){
  	if(argc != 3){
			printf("Wrong argument\n");
			return EXIT_FAILURE;
		}// check the arguments
		BMPImage * image = BMP_Open(argv[1]);
		if(image ==NULL){
			printf("Error opening BMP");
			return EXIT_FAILURE;
		}

		BMPImage * grayscale = ImgToGray(image);
		if(grayscale == NULL){
			return EXIT_FAILURE;
		}
		BMP_Write(argv[2], grayscale);
 	// open the BMP file
  // convert to gray scale
	// check for error in converting to gray scale
	BMP_Free(image);
	BMP_Free(grayscale);
	// write the gray image to file
	// free all the images
	return EXIT_SUCCESS;
}

#endif
