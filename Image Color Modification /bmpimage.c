#include "bmpimage.h"
//Include your own code from HW10 and modify this file
#ifdef TEST_HEADERVALID

int Is_BMPHeader_Valid(BMPHeader* header, FILE *fptr) {
	// use code from HW10
  if((header -> type) != 0X4D42){
  	return FALSE;
  }
  if((header -> offset) != BMP_HEADER_SIZE){
  	return FALSE;
  }
  if((header -> DIB_header_size) != DIB_HEADER_SIZE){
  	return FALSE;
  }
  if((header -> planes) != 1){
  	return FALSE;
  }
  if((header -> compression) != 0){
  	return FALSE;
  }
  if((header -> ncolours) != 0){
  	return FALSE;
  }
  if((header -> importantcolours) != 0){
  	return FALSE;
  }
  if((header -> bits) != 24){
  	return FALSE;
  }

  return TRUE;
}

#endif

#ifdef TEST_BMPOPENFILE

BMPImage *BMP_Open(const char *filename) {
  FILE *fptr = fopen(filename,"r");


  //Allocate memory for BMPImage*;

  BMPImage *bmpImage = (BMPImage *)malloc(sizeof(BMPImage));
  //check for memory allocation errors
  if (fptr == NULL){
    return NULL;
  }

  //Read the first 54 bytes of the source into the header

  int read_size = fread(&(bmpImage->header), sizeof(BMPHeader), 1, fptr);
  if(read_size != 1){
    return NULL;
  }
  if(Is_BMPHeader_Valid(&(bmpImage -> header), fptr) == 0){
    return NULL;
  }
  //check if the header is valid

  // Allocate memory for image data
  bmpImage->data = (unsigned char *)malloc(sizeof(unsigned char)*((int)((bmpImage->header).imagesize)));
  //check error
  if((bmpImage -> data) == NULL){
    return NULL;
  }

  if(fread(bmpImage -> data, sizeof(char), (bmpImage -> header).imagesize, fptr) != ((bmpImage -> header).imagesize)){
    return NULL;
  }
  // read in the image data

  //check for error while reading

  fclose(fptr);
  return bmpImage;
  }
#endif


#ifdef TEST_WRITEFUNC

int BMP_Write(const char * outfile, BMPImage* image){
  FILE *fptr = fopen(outfile, "w");
  //open file and check for error
  if(fptr == NULL){
    return FALSE;
  }
  if(fwrite(&(image -> header),sizeof(BMPHeader),1,fptr) != 1){
    fclose(fptr);
    return FALSE;
  }
  if(fwrite(image->data, sizeof(unsigned char), (image->header).imagesize, fptr) != (image -> header).imagesize){
    fclose(fptr);
    return FALSE;
  }
  //check error for writing

  // write and check for image data:(fwrite(image->data, sizeof(unsigned char), (image->header).imagesize, fptr) != (image->header).imagesize)

  fclose(fptr);
  return TRUE;
	// use code from HW10
}

#endif



/* The input argument is the BMPImage pointer. The function frees memory of
 * the BMPImage.
 */
#ifdef TEST_BMPFREEFUNC
void BMP_Free(BMPImage* image) {
  if(image != NULL){
		if(image -> data != NULL){
			free(image -> data);
		}
		free(image);
	}
	return;
	//free the data
}

#endif
