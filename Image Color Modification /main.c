#include "main.h"
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
    // open the BMP file
    // convert to gray scale
  	// check for error in converting to gray scale
    BMPImage * adaptive = AdaptiveThresholding(grayscale, radius, epsilon);
    // check for errors after calling adaptive threshold
    if(adaptive == NULL) {
      return EXIT_FAILURE;
    }

  BMP_Write(argv[2], adaptive);
  BMP_Free(image);
  BMP_Free(grayscale);// write the adaptive threshold image to file
	BMP_Free(adaptive);// free all the images
	return EXIT_SUCCESS;
}

#endif
