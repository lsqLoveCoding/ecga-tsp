# import some operators
import util.CrossoverOperators
import util.MutationOperators
import util.SelectionStrategy
ALG_NAME = 'GA'

# GA1: order_crossover & elitism_selection & swap_mutation
class GeneticAlgorithm:
    def __init__(self):
        self.name = 'ga1'
        self.mutation_operator = util.MutationOperators.swap_mutation
        self.selection_strategy = util.SelectionStrategy.elitism_selection
        self.crossover_operator = util.CrossoverOperators.order_crossover

# GA2: cycle_crossover & fitness_proportional & swap_mutation
class GeneticAlgorithmStar:
    def __init__(self):
        self.name = 'ga2'
        self.mutation_operator = util.MutationOperators.swap_mutation
        self.selection_strategy = util.SelectionStrategy.fitness_proportional
        self.crossover_operator = util.CrossoverOperators.cycle_crossover

# GA3: order_crossover & tournament_selection & scramble_mutation
class GeneticAlgorithmFinal:
    def __init__(self):
        self.name = 'ga3'
        self.mutation_operator = util.MutationOperators.scramble_mutation
        self.selection_strategy = util.SelectionStrategy.tournament_selection
        self.crossover_operator = util.CrossoverOperators.order_crossover
