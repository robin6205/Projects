TARGET = main
GCC = gcc
CFLAGS = -g -std=c99 -Wall -Wshadow -Wvla -Werror -pedantic
CC = $(GCC) $(CFLAGS)

SRCS = part.c main.c #please complete

OBJS = $(SRCS:%.c=%.o)
VALGRIND = valgrind --tool=memcheck --verbose --log-file

TESTFLAGS = -DTEST_MAIN -DTEST_CREATENODE -DTEST_LINKEDLISTCREATE -DTEST_SPLIT -DTEST_DIV -DLINKEDLIST


.c.o:
	$(CC) $(TESTFLAGS) $(CFLAGS) -c $*.c

$(TARGET): $(OBJS)
	$(CC) $(TESTFLAGS) $(OBJS) -o $(TARGET)

testmemory: $(TARGET)
	$(VALGRIND)=./valgrind.log ./main inputs/test1.txt output1.txt

testall: test1 test2 test3 test4

test1:
	./main inputs/test1.txt > output1.txt
	diff output1.txt expected/expected1.txt

test2:
	./main inputs/test2.txt > output2.txt
	diff output2.txt expected/expected2.txt
test3: 
	./main inputs/test3.txt > output3.txt
	diff output3.txt expected/expected3.txt
test4:
	./main inputs/test4.txt > output4.txt
	diff output4.txt expected/expected4.txt

clean:
	rm -f $(OBJS) $(TARGET)
