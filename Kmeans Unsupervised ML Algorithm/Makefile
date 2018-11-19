

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR)

TESTFALGS = -DTEST_CLOSESTCENTROID -DTEST_DIST -DTEST_KMEAN

SRCS = datapoint.c centroid.c main.c
OBJS = $(SRCS:%.c=%.o)

main: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o main

.c.o:
	$(GCC) $(TESTFALGS) -c $*.c

testall: test1 test2 test3 test4 test5

testadd: main
	test1
	test2
	test3
	test4
	test5


test1: main
	./Kmeans test/test1.txt 2 output1.txt
	diff -i -w output1.txt expected/expected1.txt

test2: main
	./main test/test2.txt 3 output2.txt
	diff -i -w output2.txt expected/expected2.txt

test3: main
	./hw04 test/test3.txt 4 output3.txt
	diff -i -w output3.txt expected/expected3.txt
test4: main
	./main test/test4.txt 4 output4.txt
	diff -i -w output4.txt expected/expected4.txt

test5: main
	./main test/test5.txt 10 output5.txt
	diff -i -w output5.txt expected/expected5.txt

test6: main
	./main test/test6.txt 2 output6.txt
	diff -i -w output5.txt expected/expected6.txt

test7: main
	./main test/test7.txt 2 output7.txt
	diff -i -w output5.txt expected/expected7.txt

test8: main
	./main test/test8.txt 2 output8.txt
	diff -i -w output5.txt expected/expected8.txt

clean: # remove all machine generated files
	rm -f main *.o
