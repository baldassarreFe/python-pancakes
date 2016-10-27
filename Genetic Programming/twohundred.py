import math
import random

import genetics
import matplotlib.pyplot as plt
import pandas as pd


def sum_to(value):
    def fitness(individual):
        return math.exp(-0.05 * abs(sum(individual) - value))

    return fitness


def cut_and_splice_crossover(ind1, ind2):
    point1 = random.randint(0, len(ind1) - 1)
    point2 = random.randint(0, len(ind2) - 1)
    if random.random() > 0.5:
        return ind1[:point1] + ind2[point2:]
    else:
        return ind2[:point2] + ind1[point1:]


def simple_mutation(individual):
    if random.random() < 0.1:
        point = random.randint(0, len(individual) - 1)
        individual[point] += int(individual[point] * random.uniform(-0.05, +0.05))
    return individual


def random_pop(count):
    pop = []
    for _ in range(count):
        length = random.randint(1, 3)
        pop.append(random.sample(range(50), length))
    return pop


if __name__ == '__main__':
    population = random_pop(1000)
    fitness_fn = sum_to(200)
    winners, grades, history = genetics.run(population, max_generations=1000, fitness_fn=fitness_fn,
                                            crossover_fn=cut_and_splice_crossover, mutation_fn=simple_mutation,
                                            ratio_fit=0.2, ratio_unfit=0.05, target=0.99, target_size=15)

    fig, axes = plt.subplots(nrows=2, ncols=1)

    p1 = history.plot(logx=history.shape[0] > 100, title="Fitness per generation", ax=axes[0])
    p1.set_ylabel("Fitness")
    p1.set_xlabel("Generation")

    df = pd.DataFrame(grades, index=[",".join(map(str, w[:5])) + ("..." if len(w)>5 else "") for w in winners])
    p2 = df.plot(kind="barh", legend=None, title="Genes found", ax=axes[1])
    p2.set_xlabel("Fitness")
    p2.set_xlim([0.999 * min(df[0]), 1.0])

    fig.tight_layout()
    plt.show()
