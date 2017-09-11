from util.util import *
from random import randint


class PairSelector:
    def select(self, population):
        if SELECTION_METHOD == TOURNAMENT_SELECTION:
            return self.tournament_selector(population)
        elif SELECTION_METHOD == ROULETTE_SELECTION:
            return self.roulette_selector(population)
        elif SELECTION_METHOD == RANK_SELECTION:
            return self.rank_selector(population)

    # Perform Tournament selection.
    # This is done by randomly picking a set amount of individuals from the population.
    # Then finding the best individual from that group and returning it.
    def tournament_selector(self, population):
        parents = list()
        parents.append(self.create_tournament(self.create_tournament_pool(population)))
        parents.append(self.create_tournament(self.create_tournament_pool(population)))
        return parents

    # Find the individual with the highest fitness from among a group.
    def create_tournament(self, tournament_pool):
        return get_fittest_individual(tournament_pool)

    # Create a random group of individuals who will be put into a tournament.
    def create_tournament_pool(self, population):
        tournament_pool = list()
        for i in range(TOURNAMENT_SIZE):
            tournament_pool.append(population[randint(0, POPULATION_SIZE-1)])
        return tournament_pool

    # Perform Roulette selection
    # This is done by putting all the values on a "roulette wheel" after normalization.
    # And the generating a random number to select a parent randomly from said "roulette wheel".
    # The higher the fitness, the higher the chance to be selected.
    def roulette_selector(self, population):
        parents = list()
        normaliser = self.get_normalisation_value(population)
        sum_val = self.get_normalised_fitness_sum(population, normaliser)
        parents.append(self.roulette_winner(population, normaliser, uniform(0, sum_val)))
        parents.append(self.roulette_winner(population, normaliser, uniform(0, sum_val)))
        return parents

    # Pick a winner, based on a randomly generated value, from a "roulette wheel".
    def roulette_winner(self, population, normaliser, random_value):
        partial_sum = 0.0
        for ind in population:
            partial_sum += ind.fitness + normaliser
            if partial_sum >= random_value:
                return ind

    # Find the lowest fitness in the data set.
    def get_normalisation_value(self, population):
        lowest_value = sys.maxsize
        for ind in population:
            if ind.fitness < lowest_value:
                lowest_value = ind.fitness
        return abs(lowest_value)

    # Return the total of all normalised fitness values.
    def get_normalised_fitness_sum(self, population, normaliser):
        sum_val = 0.0
        for ind in population:
            sum_val += ind.fitness + normaliser
        return sum_val

    # TODO: Perform rank selection
    def rank_selector(self, population):
        print("Rank selection has not been implemented yet.")
        print("It'll probably never happen, either.")
        sys.exit(0)

