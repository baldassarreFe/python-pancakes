import random

import genetics
import matplotlib.pyplot as plt

valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def similar_to(word):
    def fitness(individual):
        dist = sum([abs(ord(c1) - ord(c2)) for c1, c2 in zip(word, individual)])
        return 1.0 / (1.0 + dist)

    return fitness


def single_crossover(ind1, ind2):
    breakpoint = random.randint(0, len(ind1) - 1)
    return ind1[:breakpoint] + ind2[breakpoint:]


def adj_char(char):
    result = ord(char) + random.randint(-2, 2)
    if ord("A") <= result <= ord("Z"):
        return chr(result)
    else:
        return char


def simple_mutation(individual):
    chars = list(individual)
    if random.random() < 0.1:
        point = random.randint(0, len(individual) - 1)
        chars[point] = adj_char(chars[point])
        return "".join(chars)
    else:
        return individual


def random_pop(length, count):
    pop = []
    for _ in range(count):
        pop.append(''.join(random.choice(valid_chars) for _ in range(length)))
    return pop


if __name__ == '__main__':
    secret_word = "GENETICALGORITHMSAREGREATATGUESSINGVERYLONGWORDS"
    population = random_pop(len(secret_word), 1000)
    winners, grades, history = genetics.run(population, max_generations=1000, fitness_fn=similar_to(secret_word),
                                            crossover_fn=single_crossover, mutation_fn=simple_mutation,
                                            ratio_fit=0.2, ratio_unfit=0.05, target=0.99)

    p1 = history.plot(logx=history.shape[0] > 100, title="Fitness per generation")
    p1.set_ylabel("Fitness")
    p1.set_xlabel("Generation")
    plt.show()
    print(winners[0])
