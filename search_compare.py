import argparse
import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False 

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
            return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(sorted(a_list)) and not found and not stop:
        if sorted(a_list)[pos] == item:
            found = True
        else:
            if sorted(a_list)[pos] > item:
                stop = True
    else:
        pos = pos+1
        return found


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
            return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)


if __name__ == "__main__":
    """Main Entry Point"""
#sequential search times for 500, 1000, and 5000 elements

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(500)
        start = time.time()
        sequential_search(mylist500, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of 500 elements.")

    total_time = 0
    for i in range(100):
        mylist1000 = get_me_random_list(1000)
        start = time.time()
        sequential_search(mylist1000, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of 1000 elements.")

    total_time = 0
    for i in range(100):
        mylist5000 = get_me_random_list(5000)
        start = time.time()
        sequential_search(mylist5000, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of 5000 elements.")

#ordered sequential search times for 500, 1000, and 5000 elements

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(500)
        start = time.time()
        ordered_sequential_search(mylist500, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"ordered sequential search took {avg_time:10.7f} seconds to run, on average for a list of 500 elements.")

    total_time = 0
    for i in range(100):
        mylist1000 = get_me_random_list(1000)
        start = time.time()
        ordered_sequential_search(sorted(mylist1000), -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"ordered sequential search took {avg_time:10.7f} seconds to run, on average for a list of 1000 elements.")

    total_time = 0
    for i in range(100):
        mylist5000 = get_me_random_list(5000)
        start = time.time()
        ordered_sequential_search(mylist5000, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"ordered sequential search took {avg_time:10.7f} seconds to run, on average for a list of 5000 elements.")

#binary iterative search times for 500, 1000, and 5000 elements

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(500)
        start = time.time()
        binary_search_iterative(mylist500, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"binary iterative search took {avg_time:10.7f} seconds to run, on average for a list of 500 elements.")

    total_time = 0
    for i in range(100):
        mylist1000 = get_me_random_list(1000)
        start = time.time()
        binary_search_iterative(mylist1000, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"binary iterative search took {avg_time:10.7f} seconds to run, on average for a list of 1000 elements.")

    total_time = 0
    for i in range(100):
        mylist5000 = get_me_random_list(5000)
        start = time.time()
        binary_search_iterative(mylist5000, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"binary iterative search took {avg_time:10.7f} seconds to run, on average for a list of 5000 elements.")

#binary recursive search times for 500, 1000, and 5000 elements

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(500)
        start = time.time()
        binary_search_recursive(mylist500, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"binary recursive search took {avg_time:10.7f} seconds to run, on average for a list of 500 elements.")

    total_time = 0
    for i in range(100):
        mylist1000 = get_me_random_list(1000)
        start = time.time()
        binary_search_recursive(mylist1000, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"binary recursive search took {avg_time:10.7f} seconds to run, on average for a list of 1000 elements.")

    total_time = 0
    for i in range(100):
        mylist5000 = get_me_random_list(5000)
        start = time.time()
        binary_search_recursive(mylist5000, -1)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"binary recursive search took {avg_time:10.7f} seconds to run, on average for a list of 5000 elements.")
