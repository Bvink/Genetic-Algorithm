from util.util import *


class Elitism:

    # Perform Elitism.
    # This is done by returning the (in this case) two individuals with the highest fitness.
    # Then ensuring that those are put back into the population.
    def get_highest_x_elites(self, population, x):
        return order_individuals_by_fitness(population)[:x]



