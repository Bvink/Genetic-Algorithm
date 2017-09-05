from objects.individual import *
from random import *


def get_fittest_individual(individuals):
    chosen_ind = Individual([])
    chosen_ind.fitness = -1
    for ind in individuals:
        if ind.fitness > chosen_ind.fitness:
            chosen_ind = ind
    return chosen_ind


def order_individuals_by_fitness(individuals):
    unordered = individuals
    ordered = []
    i = 0

    highest = unordered[0]

    while len(unordered) > 0:
        if unordered[i].fitness > highest.fitness:
            highest = unordered[i]
        i += 1
        if i == len(unordered):
            ordered.append(highest)
            unordered.remove(highest)
            if unordered:
                highest = unordered[0]
            i = 0
    return ordered


def get_average_fitness(individuals):
    sum_val = 0
    for ind in individuals:
        sum_val += ind.fitness
    return sum_val / POPULATION_SIZE


def random_double(lowerbound, upperbound):
    return uniform(lowerbound, upperbound)
