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

//Modify below this line and use code from HW10 for IMGTOGRAY()

#ifdef TEST_IMGTOGRAY

BMPImage * ImgToGray(BMPImage * image){

	// use code from your HW10
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

//Write your own code for Adaptive Thresholding Function
#ifdef TEST_ADAPTIVETHRESHOLDING

BMPImage * AdaptiveThresholding(BMPImage * grayImage, int radius, int epsilon){
 	BMPImage *adaptive = (BMPImage *)malloc(sizeof(BMPImage));// allocate space for the image
	// the image has the same size(height and width)
	// therefore the header has to stay the same

	adaptive->header = grayImage->header;
	// (gray_image->header).imagesize = (gray_image->header).width*(gray_image->header).height;
	if ((adaptive->data = malloc(sizeof(unsigned char)*(adaptive->header).imagesize)) == NULL) {
		fprintf(stderr, "Error allocating memory\n");
		free(adaptive);
		return NULL;
	}

	//int pixel=0;
	//Run a nested loop for all elements using height and width
        //Find the maximum of top row, bottom rpw, left column and right column using radius
				int height = (grayImage -> header).height;
					int width = (grayImage -> header).width;
					int pixel=0;
					//Run a nested loop for all elements using height and width
					for(int row = 0; row < height; row++) {
						for(int col = 0; col < width; col++) { //increment by 3?
							int sum = 0;
							int counter = 0;
					  	//Find the maximum of top row, bottom rpw, left column and right column using radius
							int toprow = MAX(0, row-radius);
					  	int bottomrow = MIN(height-1, row+radius);
							int leftcol = MAX(0, col-radius);
					  	int rightcol = MIN(width-1, col+radius);
					  	//Calculate the average of all pixels
							//Run loop from toprow to bottom row
							for(int i = toprow; i <= bottomrow; i++) {
								for(int j = leftcol; j <= rightcol; j++) {
									sum += grayImage -> data[(i * width + j) * 3];
									counter++;
								}
							}
							int average = sum / counter;
							pixel = (row * width + col) * 3;
							if ((average - epsilon) > (grayImage -> data[pixel])) {
								(adaptive -> data)[pixel] = 0; //black
								(adaptive -> data)[pixel+1] = 0;
								(adaptive -> data)[pixel+2] = 0;
							} else if ( (average - epsilon) <= (grayImage -> data[pixel]) ) {
								(adaptive -> data)[pixel] = 255; //white
								(adaptive -> data)[pixel+1] = 255;
								(adaptive -> data)[pixel+2] = 255;
							}
        // else if average is lower then color shall be white(255) for data value at pixel, pixel+1, pixel+
//return the image after adaptive thresholding

}
}
return adaptive;
}



#endif
