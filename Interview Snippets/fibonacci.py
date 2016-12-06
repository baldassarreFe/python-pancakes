def fibonacci_rec(n):
    if n in [0, 1]:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter1(n):
    solutions = [0, 1]
    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])
    return solutions[n]


def fibonacci_iter_2(n):
    if n in [0, 1]:
        return n
    minus2 = 0
    minus1 = 1
    for _ in range(2, n + 1):
        minus2, minus1 = minus1, minus1 + minus2
    return minus1


def fibonacci_gen(n):
    minus2 = 0
    minus1 = 1
    for i in range(n):
        if i in [0, 1]:
            yield i
        else:
            minus2, minus1 = minus1, minus1 + minus2
            yield minus1


rec = [fibonacci_rec(i) for i in range(10)]
iter1 = [fibonacci_iter1(i) for i in range(10)]
iter2 = [fibonacci_iter_2(i) for i in range(10)]
gen = list(fibonacci_gen(10))

print(rec)
print(iter1)
print(iter2)
print(gen)
