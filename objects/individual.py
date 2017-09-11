from settings.gensettings import *
from random import randint
from math import *


class Individual(object):

    def __init__(self, dna):
        if not self.confirm_dna(dna):
            dna = self.set_dna()
        self.dna = dna
        self.real_value = self.real_value(dna)
        self.fitness = self.calc_fitness(self.real_value)

    def confirm_dna(self, dna):
        if len(dna) == DNA_SIZE:
            for i in dna:
                if not i == 1 or i == 0:
                    return bool(0)
            return bool(1)
        return bool(0)

    def set_dna(self):
        dna = list()
        for i in range(DNA_SIZE):
            dna.append(randint(0, 1))
        return dna

    def real_value(self, dna):
        real_value = 0
        for i in range(len(dna)):
            real_value += dna[i] * math.pow(2, len(dna) - i - 1)
        return int(real_value)

    def calc_fitness(self, real_value):
        return fitness(real_value)
