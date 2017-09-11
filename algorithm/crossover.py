from objects.individual import *
from constants.constants import *
from random import *


class Crossover:
    def crossover(self, parents):
            if uniform(0, 1) <= CROSSOVER_RATE:
                child_dna = list()
                child_dna.append([0] * DNA_SIZE)
                child_dna.append([0] * DNA_SIZE)

                if CROSSOVER_METHOD == SINGLE_POINT_CROSSOVER_INDEX:
                    Tester = type('Tester', (), {"test": lambda self, i: i < SINGLE_POINT_CROSSOVER_INDEX})
                    child_dna = self.perform_crossover(parents, child_dna, Tester())
                elif CROSSOVER_METHOD == TWO_POINT_CROSSOVER:
                    Tester = type('Tester', (), {"test": lambda self, i: i < TWO_POINT_CROSSOVER_INDICES[0] | i > TWO_POINT_CROSSOVER_INDICES[1]})
                    child_dna = self.perform_crossover(parents, child_dna, Tester())
                elif CROSSOVER_METHOD == UNIFORM_CROSSOVER:
                    Tester = type('Tester', (), {"test": lambda self, i: bool(randint(0, 1))})
                    child_dna = self.perform_crossover(parents, child_dna, Tester())

                children = list()
                children.append(Individual(child_dna[0]))
                children.append(Individual(child_dna[1]))
                return children
            return parents

    # Perform crossover to create children from two parents.
    def perform_crossover(self, parents, child_dna, tester):
        for i in range(DNA_SIZE):
            child_dna = self.cross(parents, child_dna, i, tester.test(i))
        return child_dna

    # Perform the crossover on a single bit of DNA.
    def cross(self, parents, child_dna, i, test):
        if test:
            child_dna[0][i] = parents[0].dna[i]
            child_dna[1][i] = parents[1].dna[i]
        else:
            child_dna[0][i] = parents[1].dna[i]
            child_dna[1][i] = parents[0].dna[i]
        return child_dna
