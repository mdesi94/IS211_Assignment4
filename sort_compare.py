import argparse
import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    for index in range(1, len(a_list)):

        currentvalue = a_list[index]
        position = index

        while position>0 and a_list[position-1]>currentvalue:
            a_list[position]=a_list[position-1]
            position = position-1

        a_list[position] = currentvalue


def shell_sort(a_list):
    sublistcount = len(a_list) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount)

        sublistcount = sublistcount // 2


def gapInsertionSort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):

        currentvalue = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > currentvalue:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = currentvalue


def python_sort(a_list):
    return sorted(a_list)


if __name__ == "__main__":
    """Main entry point"""

#generate 100 random lists and determine avg time to run for each list size using insertion sort

list_sizes = [200, 500, 1000]
for size in list_sizes:
    total_time = 0
    for i in range(100):
        start = time.time()
        insertion_sort(get_me_random_list(size))
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {size} elements.")

#generate 100 random lists and determine avg time to run for each list size using shell sort
list_sizes = [200, 500, 1000]
for size in list_sizes:
    total_time = 0
    for i in range(100):
        start = time.time()
        shell_sort(get_me_random_list(size))
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"shell sort took {avg_time:10.7f} seconds to run, on average for a list of {size} elements.")

#generate 100 random lists and determine avg time to run for each list size using builtin python sort
list_sizes = [200, 500, 1000]
for size in list_sizes:
    total_time = 0
    for i in range(100):
        start = time.time()
        python_sort(get_me_random_list(size))
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"python sort took {avg_time:10.7f} seconds to run, on average for a list of {size} elements.")