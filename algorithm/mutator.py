from objects.individual import *
from random import uniform


class Mutator:
    # Mutate an individual's gene at a set percentage chance.
    def mutate(self, individual):
        dna = individual.dna
        i = 0
        while i < len(dna):
            if uniform(0, 1) < MUTATION_RATE:
                dna[i] ^= 1
            i += 1
        return Individual(dna)
