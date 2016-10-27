import random
import pandas as pd
import functools


def grade_and_sort(population, fitness_fn):
    return


def breed(ind1, ind2, crossover_fn, mutation_fn):
    return mutation_fn(crossover_fn(ind1, ind2))


def evolve(selection, size, crossover_fn, mutation_fn):
    next_gen = []
    breeding_fn = functools.partial(breed, crossover_fn=crossover_fn, mutation_fn=mutation_fn)
    for _ in range(size - len(selection)):
        ind1, ind2 = random.sample(selection, 2)
        next_gen.append(breeding_fn(ind1, ind2))
    return next_gen + list(map(mutation_fn, selection))


def run(population, max_generations, fitness_fn, crossover_fn, mutation_fn,
        ratio_fit=0.2, ratio_unfit=0.05, target=0.9, target_size=1):
    n = len(population)
    fit = int(n * ratio_fit)
    unfit = int(n * ratio_unfit)

    history = pd.DataFrame(columns=["Avg fit", "Target fit", "Best sol"])

    for t in range(max_generations):
        population, grades = zip(
            *sorted([(ind, fitness_fn(ind)) for ind in population], key=lambda i_f: i_f[1], reverse=True))
        population = list(population)
        grades = list(grades)
        target_fitness = sum(grades[:target_size])/target_size
        history.loc[t] = pd.Series([sum(grades) / n, target_fitness, population[0]],
                                   index=["Avg fit", "Target fit", "Best sol"])

        if target_fitness > target:
            break

        selection = population[:fit] + random.sample(population[fit:], unfit)
        population = evolve(selection, n, crossover_fn=crossover_fn, mutation_fn=mutation_fn)

    return population[:target_size], grades[:target_size], history
