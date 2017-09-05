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
                    child_dna = self.single_point_crossover(parents, child_dna)
                elif CROSSOVER_METHOD == TWO_POINT_CROSSOVER:
                    child_dna = self.two_point_crossover(parents, child_dna)
                elif CROSSOVER_METHOD == UNIFORM_CROSSOVER:
                    child_dna = self.uniform_crossover(parents, child_dna)

                children = list()
                children.append(Individual(child_dna[0]))
                children.append(Individual(child_dna[1]))
                return children
            return parents

    # Perform single point crossover to create children from two parents.
    # Single point crossover is performed by taking bits from either parents based on a single crossover points.
    def single_point_crossover(self, parents, child_dna):
        i = 0
        while i < DNA_SIZE:
            test = i < SINGLE_POINT_CROSSOVER_INDEX
            child_dna = self.cross(parents, child_dna, i, test)
            i += 1
        return child_dna

    # Perform two point crossover to create children from two parents.
    # Two point crossover is performed by taking bits from either parents based on two crossover points.
    def two_point_crossover(self, parents, child_dna):
        i = 0
        while i < DNA_SIZE:
            test = i < TWO_POINT_CROSSOVER_INDICES[0] | i > TWO_POINT_CROSSOVER_INDICES[1]
            child_dna = self.cross(parents, child_dna, i, test)
            i += 1
        return child_dna

    # Perform uniform crossover to create children from two parents.
    # Uniform crossover is performed by randomly taking bits from either parents.
    def uniform_crossover(self, parents, child_dna):
        i = 0
        while i < DNA_SIZE:
            test = randint(0, 1) == 0
            child_dna = self.cross(parents, child_dna, i, test)
            i += 1
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
