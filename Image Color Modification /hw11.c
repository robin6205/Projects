#include "hw11.h"
//Modify this file
#ifdef TEST_MAIN

int main(int argc, char **argv){
  if (argc != 5) {
  printf("Wrong arguments\n");
  return EXIT_FAILURE;
  }
  int radius = strtol(argv[3], NULL, 10);
  int epsilon = strtol(argv[4], NULL, 10);
  if ((radius == 0 )||( epsilon == 0)){
    printf("Wrong inputs");
    return EXIT_FAILURE;
  }

		BMPImage * image = BMP_Open(argv[1]);
		if(image ==NULL){
			printf("Error opening BMP file\n");
			return EXIT_FAILURE;
		}

		BMPImage * grayscale = ImgToGray(image);
		if((grayscale == NULL) || (grayscale == 0)){
			return EXIT_FAILURE;
		}

    BMPImage * adaptive = AdaptiveThresholding(grayscale, radius, epsilon);
    // check for errors after calling adaptive threshold
    if(adaptive == NULL) {
      return EXIT_FAILURE;
    }
// write the adaptive threshold image to file

 	// open the BMP file
  // convert to gray scale
	// check for error in converting to gray scale

	// write the gray image to file
	// free all the images


  // check the arguments - please read readme about validity of arguments
  // check radius and epsilon values -  read readme for the validity of argument
  // open the BMP file
  // convert to gray scale
	// check for error in converting to gray scale

  // call adaptive threshold function
  // check for errors after calling adaptive threshold
  BMP_Write(argv[2], adaptive);
  BMP_Free(image);
  BMP_Free(grayscale);// write the adaptive threshold image to file
	BMP_Free(adaptive);// free all the images
	return EXIT_SUCCESS;
}

#endif
