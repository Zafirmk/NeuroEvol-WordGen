import random
import math  # For Fitness Function 2
import string
from Settings import *


class DNA:  # Class of each object (word) generated
    def __init__(self):
        self.probability = 0
        self.fitness = 0
        self.char_list = []

    # Calculates likelihood of reproduction. [Fitness Function 1]
    def CalculateFitness(self):
        for k in range(0, len(target_list)):
            if self.char_list[k] == target_list[k]:
                self.fitness += 1
        self.probability = int(self.fitness * 100)

    # Alternate fitness function (Requires greater computational power) [Fitness Function 2]
    '''
        def CalculateFitness(self): 
        for k in range(0, len(target_list)):
            if self.char_list[k] == target_list[k]:
                self.fitness += 1
        self.probability = int(math.exp(self.fitness))
    '''

    # Fuses two DNA Objects together.
    def Breed(self, ParentB):
        splitter = random.randint(0, (self.char_list.__len__()) - 1)
        ParentA_halve = self.char_list[:splitter]
        ParentB_halve = ParentB.char_list[splitter:]
        child_list = ParentA_halve + ParentB_halve
        child = DNA()
        child.char_list = child_list
        return child

    # Randomly causes a genetic change in a DNA Object.
    # (ie: Randomly replaces a character in the char_list of a DNA object
    def Mutation(self):
        if random.random() <= mutation_rate:
            for k in range(0, len(target_list)):
                if self.char_list[k] != target_list[k]:
                    index = random.randint(0, self.char_list.__len__() - 1)
                    self.char_list[index] = random.choice(string.ascii_letters)
        else:
            pass
