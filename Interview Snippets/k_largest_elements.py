import heapq
import random


def k_largest_heap(l, k):
    '''Finds all the k largest numbers in a list'''
    result = []
    for i in l:
        if len(result) < k:
            heapq.heappush(result, i)
        else:
            heapq.heappushpop(result, i)
    return result


def k_largest_quickselect(l, k):
    '''Finds the k-th largest number in a list'''
    pivot = random.choice(l)
    smaller = []
    larger = []
    for i in l:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            larger.append(i)
    if len(larger) + 1 > k:
        return k_largest_quickselect(larger, k)
    elif len(larger) + 1 < k:
        return k_largest_quickselect(smaller, k - 1 - len(larger))
    else:
        return pivot


def k_smallest_heap(l, k):
    '''Finds all the k smallest numbers in a list'''
    result = []
    for i in l:
        if len(result) < k:
            heapq.heappush(result, -i)
        else:
            heapq.heappushpop(result, -i)
    return [-i for i in result]


def k_smallest_quickselect(l, k):
    '''Finds the k-th smallest number in a list'''
    pivot = random.choice(l)
    smaller = []
    larger = []
    for i in l:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            larger.append(i)
    if len(smaller) + 1 > k:
        return k_smallest_quickselect(smaller, k)
    elif len(smaller) + 1 < k:
        return k_smallest_quickselect(larger, k - 1 - len(smaller))
    else:
        return pivot


l = random.sample(range(10), 5)

print(sorted(l))
print()
for k in range(1, len(l) + 1):
    print(k, "largest:", sorted(k_largest_heap(l, k)), "->", k_largest_quickselect(l, k))

print()
for k in range(1, len(l) + 1):
    print(k, "smallest:", sorted(k_smallest_heap(l, k)), "->", k_smallest_quickselect(l, k))
