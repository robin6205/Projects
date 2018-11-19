TARGET = hw11
GCC = gcc
CFLAGS = -g -std=c99 -Wall -Wshadow -Wvla -Werror -pedantic
CC = $(GCC) $(CFLAGS)

SRCS = bmpimage.c hw11.c bmpfunc.c 

OBJS = $(SRCS:%.c=%.o)
VALGRIND = valgrind --tool=memcheck --verbose --log-file

TESTFLAGS = -DTEST_MAIN -DTEST_FUNCGIVEN -DTEST_IMGTOGRAY -DTEST_ADAPTIVETHRESHOLDING -DTEST_HEADERVALID -DTEST_BMPOPENFILE -DTEST_WRITEFUNC -DTEST_BMPFREEFUNC

.c.o:
	$(CC) $(TESTFLAGS) $(CFLAGS) -c $*.c

$(TARGET): $(OBJS)
	$(CC) $(TESTFLAGS) $(OBJS) -o $(TARGET)

testmemory: $(TARGET)
	$(VALGRIND)=./valgrind.log ./hw11 exampleImages/CondProb.bmp output1.bmp

testall: test1 test2 test3 test4

test1: hw11
	./hw11 exampleImages/CondProb.bmp output1.bmp 1 2
	diff output1.bmp expectedImages/expectedCondProb.bmp

test2: hw11
	./hw11 exampleImages/RV.bmp output2.bmp 5 2
	diff output2.bmp expectedImages/expectedRV.bmp

test3: hw11
	./hw11 exampleImages/RV2.bmp output3.bmp 3 2
	diff output3.bmp expectedImages/expectedRV2.bmp

test4: hw11
	./hw11 exampleImages/RV2Small.bmp output4.bmp 11 2
	diff output4.bmp expectedImages/expectedRV2Small.bmp

clean:
	rm -f $(OBJS) $(TARGET)
