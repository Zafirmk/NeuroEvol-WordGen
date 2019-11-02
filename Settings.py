# String that is to be generated.
target = "Sample"
target_list = list(target)

# Num of DNA objects per population.
gen_size = 100
generation_num = 0

# Likelihood of mutation of a DNA object.
mutation_rate = 0.02

# Initializing states of the mating pool and population.
this_population = []
current_mating_pool = []
found = False
