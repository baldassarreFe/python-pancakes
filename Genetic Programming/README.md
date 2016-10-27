# Genetic Algorithms

## General usage
Genetic algorithms can be broken down to the following components:

<dl>
  <dt>Individual</dt>
  <dd>An element representing the genes, can be a list of numbers, a sequence of characters...</dd>

  <dt>Population</dt>
  <dd>A collection of individuals that will be subject to evaluation and evolution</dd>

  <dt>Fitness function</dt>
  <dd>Used to grade each individual of the population on the base of how fit it is to solve a given problem</dd>

  <dt>Selection function</dt>
  <dd>A function that selects the most fit individuals for reproduction</dd>

  <dt>Breeding function</dt>
  <dd>A function that controls how the population of a generation evolves into the next one</dd>

  <dt>Crossover function</dt>
  <dd>A function that combines two genes generating one individual as the offspring</dd>

  <dt>Mutation function</dt>
  <dd>A function that introduces random variations into the genes of an individual</dd>
</dl>

The main script ```genetics.py``` contains the skeleton code for evolving a solution for any kind of genetic problem.

The evolution process is fully taken care of by the core script: handling the selection process and the evolution of the population. The user only needs to define the individuals and the fitness, crossover and mutation functions.

The fitness function must output a value between 0 and 1, with 1 indicating a perfect fit.
The crossover function must output the offspring of two individuals.
The mutation function can alter the genes of one individual.

The function ```run``` is defined as follows:
```python
run(population, max_generations, fitness_fn, crossover_fn, mutation_fn, ratio_fit=0.2, ratio_unfit=0.05, target=0.9, target_size=1)
```

It takes as input the initial population, the maximum number of generations to evolve and functions to use to generate the new individuals.

Optionally one can specify the ratio of fit and unfit individuals selected to generate the next generation. Moreover it's possible to tweak the convergence parameters, specifying the minimum desired value of the fitness function and the number of individuals that on average must be over this value.

Finally, note that the whole process is problem-agnostic, i.e. it can deal with any type of individual, population and functions.

## Examples
### A list of number that sums to 200
See the ```twohundred.py``` file.

Consider a list of integers as an individual. The main goal is to evolve lists of any length such that the sum of their numbers is 200.

For this reason the fitness function is defined as ```e^(-0.05 * abs(200 - sum(list)))```

The crossover function will take two lists, split them on two random points and output the concatenation of one piece from the first list and one piece from the second list (Cut and splice<sup id="a1">[1](#f1)</sup>). In this way we obtain a child list that is different in length from the parents.

The mutation function will select a random number in the list and change it positively or negatively by a quantity no greater that its 5%.

### A fixed-length string that resembles a given one
See the ```letters.py``` file.

Consider a fixed length string as an individual, composed of only uppercase letters. The main goal is to evolve a string that is as similar as possible to a given string: ```GENETICALGORITHMSAREGREATATGUESSINGVERYLONGWORDS```.

For this reason the fitness function is defined as ```1/(1+dist(goal, string))```, where ```dist``` indicates the distance between the two strings, computed as the sum of the character-wise distances.

The crossover function will perform a single point crossover<sup id="a1">[1](#f1)</sup> between the two parents, selecting a random point to swap the tails of the parents.

The mutation function will shift a random letter by one or two positions, negatively or positively.

## Credits
Some of the basic ideas about genetic algorithms and the 200 example are taken from [this](http://lethain.com/genetic-algorithms-cool-name-damn-simple) tutorial.

1. <a id="f1">Crossover functions on  [Wikipedia](https://en.wikipedia.org/wiki/Crossover_%28genetic_algorithm%29)</a> [↩](#a1)
