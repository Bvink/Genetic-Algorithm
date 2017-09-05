from util.util import *


def printer(population):
    print("Genetic Algorithm")
    print_average_fitness(population)
    print_best_individual(population)


def print_average_fitness(population):
    print("The average fitness is: ")
    print(get_average_fitness(population))


def print_best_individual(population):
    best = get_fittest_individual(population)
    print("The best individual has a fitness of:")
    print(best.fitness)
    print("And a value of:")
    print(best.real_value)
    print("its DNA sequence is:")
    print(best.dna)
