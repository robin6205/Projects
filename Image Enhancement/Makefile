TARGET = main
GCC = gcc
CFLAGS = -g -std=c99 -Wall -Wshadow -Wvla -Werror -pedantic
CC = $(GCC) $(CFLAGS)

SRCS = bmpimage.c main.c bmpfunc.c #please complete

OBJS = $(SRCS:%.c=%.o)
VALGRIND = valgrind --tool=memcheck --verbose --log-file

TESTFLAGS = -DTEST_MAINFUNC -DTEST_FUNCGIVEN -DTEST_IMGTOGRAY -DTEST_HEADERVALID -DTEST_BMPOPENFILE -DTEST_BMPWRITEFUNC -DTEST_BMPFREEFUNC  #please complete

.c.o:
	$(CC) $(TESTFLAGS) $(CFLAGS) -c $*.c

$(TARGET): $(OBJS)
	$(CC) $(TESTFLAGS) $(OBJS) -o $(TARGET)

testmemory: $(TARGET)
	$(VALGRIND)=./valgrind.log ./main exampleImages/CondProb.bmp output1.bmp

testall: test1 test2 test3 test4

test1:
	./main exampleImages/CondProb.bmp output1.bmp
	diff output1.bmp expectedImages/expectedCondProb.bmp

test2:
	./main exampleImages/RV.bmp output2.bmp
	diff output2.bmp expectedImages/expectedRV.bmp

test3:
	./main exampleImages/RV2.bmp output3.bmp
	diff output3.bmp expectedImages/expectedRV2.bmp

test4: 
	./main exampleImages/RV2Small.bmp output4.bmp
	diff output4.bmp expectedImages/expectedRV2Small.bmp

clean:
	rm -f $(OBJS) $(TARGET)
