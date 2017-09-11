from util.printer import *
from algorithm.genetic_algorithm import *


class Genetic(object):

    def __init__(self):
        population = list()
        if POPULATION_SIZE & 1 == 0:
            population = self.populate(population)
            population = self.iterate(population)
            printer(population)

    # Create the initial population.
    def populate(self, population):
        i = 0
        while i < POPULATION_SIZE:
            ind = Individual([])
            population.append(ind)
            i += 1
        return population

    # Perform the genetic algorithm a set amount of times.
    def iterate(self, population):
        i = 0
        while i < ITERATIONS:
            algorithm = GeneticAlgorithm(population)
            population = algorithm.children
            i += 1
        return population

import time
start_time = time.time()
gen = Genetic()
print("--- %s seconds ---" % (time.time() - start_time))