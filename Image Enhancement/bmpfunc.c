#include "bmpfunc.h"
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

#ifdef TEST_FUNCGIVEN

int RGB2Gray(unsigned char red, unsigned char green, unsigned char blue){
	// this is a commonly used formula
	int gray = 0.2989 * red + 0.5870 * green + 0.1140 * blue;
	return gray;
}

#endif

//Modify below this line
#ifdef TEST_IMGTOGRAY

BMPImage * ImgToGray(BMPImage * image){
	//int width = (image->header).width;
	//int height = (image->header).height;

	BMPImage *gray_image = (BMPImage *)malloc(sizeof(BMPImage));// allocate space for the image
	// the image has the same size
	// therefore the header has to stay the same
	// check for memory allocation failure
	if(gray_image == NULL){
		return NULL;
	}
	//gray_image can be the name of the new image memory allotment
	gray_image->header = image->header;

	//Assign the the imagesize as height * width
	//(gray_image->header).imagesize = (gray_image->header).width*(gray_image->header).height;

	//check for data allocation failure using :
	if((gray_image->data = malloc(sizeof(unsigned char)*(gray_image->header).imagesize))==NULL){
		return NULL;
	}

	int pixel=0;
	//Run loop for all pixels using height and width
	//convert each pixel of all channels to gray using the given RGB2GRAY function
	int gray_val;
	for(int i=0; i < (gray_image -> header).width ; i++){
		for(int a=0; a <(gray_image -> header).height; a++){
	gray_val = RGB2Gray(image -> data[pixel+2],image -> data[pixel + 1],	image -> data[pixel]);
	//assign values to all pixels of gray_image for each channel
	gray_image->data[pixel+2] = gray_val;
	gray_image->data[pixel+1] = gray_val;
	gray_image->data[pixel] = gray_val;
	pixel+=3;
}
}
	//pixel+=3 to move on to the next 3 channel combination

	return gray_image;

}

#endif
