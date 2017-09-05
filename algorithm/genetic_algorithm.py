from algorithm.pair_selector import *
from algorithm.crossover import *
from algorithm.mutator import *
from algorithm.elitism import *


class GeneticAlgorithm:
    def __init__(self, population):
        self.children = list()
        self.pair_selector = PairSelector()
        self.crossover = Crossover()
        self.mutator = Mutator()

        self.children = self.create_children(population)

        if ELITISM:
            self.children.extend(self.add_elites(population))

    # Create the children to be added to the new population.
    def create_children(self, population):
        children = list()
        pairings = self.calc_pairings()
        i = 0
        while i < pairings:
            pair = self.pair_selector.select(population)
            new_children = self.crossover.crossover(pair)
            for child in new_children:
                children.append(self.mutator.mutate(child))
            i += 1
        return children

    # Calculate how many pairings there will be.
    # This is dependant on Elitism, as to not increase the initial population size.
    def calc_pairings(self):
        pairings = POPULATION_SIZE / 2
        if ELITISM:
            pairings -= 1
        return pairings

    # Add the relevant amount of elites to the new generation.
    def add_elites(self, population):
        elitism = Elitism()
        return elitism.get_highest_x_elites(population, ELITISM_COUNT)
