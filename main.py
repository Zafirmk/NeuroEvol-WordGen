from DNAClass import DNA
from Settings import *
import random
import string
import time


# Function to generate the Original generation (ie: Generation 0)
def Setup():
    print('ORIGINAL')
    for x in range(0, gen_size):
        this_population.append(DNA())  # Appends gen_size num of empty DNA Objects.
        # Generates random words with the same length as the target word
        this_population[x].char_list = random.choices(string.ascii_letters, k=target_list.__len__())
        print(''.join(this_population[x].char_list))
    print("-" * 150)
    print("-" * 150)


def MateAndCreateNewPop():
    global current_mating_pool

    # Calculate the fitness of each DNA Object in this_population
    for x in range(0, len(this_population)):
        this_population[x].CalculateFitness()

    # Create a mating pool such that the probability of an object mating is consistent with it's fitness.
    # Each object is appended to the mating_pool n times, where n is it's probability to mate (given by it's fitness)
    for x in range(0, len(this_population)):
        if this_population[x].fitness > 0:
            current_mating_pool.append(this_population[x].probability * [this_population[x]])
    current_mating_pool = sum(current_mating_pool, [])

    # Clear the current population
    this_population.clear()

    # Randomly select two parents and call the Breed and Mutate functions on them.
    # Append the child back to this_population and clear the current_mating_pool.
    while len(this_population) < gen_size:
        parentA = current_mating_pool[random.randint(0, len(current_mating_pool) - 1)]
        parentB = current_mating_pool[random.randint(0, len(current_mating_pool) - 1)]
        current_child = parentA.Breed(parentB)
        current_child.Mutation()
        this_population.append(current_child)
    current_mating_pool.clear()

    for x in range(0, len(this_population)):
        print(''.join(this_population[x].char_list))
    print("-" * 150)
    print("-" * 150)


Setup()
time.sleep(1)

# Loop until the correct word is NOT Generated.
# Keep calling the MateAndCreateNewPop() function repeatedly.
while not found:
    for x in range(0, len(this_population)):
        if this_population[x].char_list == target_list:
            found = True
    generation_num += 1
    print(generation_num)
    MateAndCreateNewPop()
