import heapq
import random
import string


def read_from_file(name):
    with open(name, mode="r") as file:
        for line in file:
            yield line.strip()


def random_words(n_words):
    for _ in range(n_words):
        yield "".join([random.choice(string.ascii_lowercase) for _ in range(3)])


if __name__ == '__main__':
    '''Finds the 10 most frequent words in a file'''
    dic = {}
    for w in random_words(1000000):
        dic[w] = dic.get(w, 0) + 1

    heap = []
    for w, f in dic.items():
        if len(heap) < 10:
            heapq.heappush(heap, (f, w))
        else:
            if heap[0][0] < f:
                heapq.heappushpop(heap, (f, w))

    print(heap)
    for f, w in heap:
        print(w, f)
