# ecga-tsp

### Exercise 1 Problem Representation and TSPlib
Write a class TSPProblem which represents the TSP problem. Your class should enable the construction of TSP problems from the ﬁles of the symmetric traveling salesperson problem of the TSPlib, which is available online:
For the problem files: http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/tsp/ The TSP main page has more information for you, if you want to read a bit: http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/

### Exercise 2 Individual and Population Representation 
Represent a possible solution to the TSP as a permutation of the given cities and implement it in a class Individual. Evolutionary algorithms often start with solutions that are constructed uniformly at random. Write a method that constructs such a solution in linear time – not in O(n log n) or even O(n2), but in O(n), where n is the number of cities. A population in an evolutionary algorithms represents a set of solutions. Implement a class Population for representing a population which is a set of individuals. Make sure that you can evaluate the quality of a solution with respect to a given problem.

### Exercise 3 Variation operators 
 • Implement the diﬀerent mutation operators (insert, swap, inversion, scramble) for permutations given in the lecture. 
 • Implement the diﬀerent crossover operators (Order Crossover, PMX Crossover, Cycle Crossover, Edge Recombination) for permutations given in the lecture.
 
### Exercise 4 Selection 
Implement the diﬀerent selection methods (ﬁtness-proportional, tournament selection, elitism) given in the lecture.

### Exercise 5 Evolutionary Algorithms and Benchmarking 
• Design three diﬀerent evolutionary algorithms using crossover and mutation, based on the implementation of your diﬀerent modules. 
• (Experiment 1) Run your three algorithms with population sizes 10,20,50,100 on the instances EIL51, EIL76, EIL101, ST70, KROA100, KROC100, KROD100, LIN105, PCB442, PR2392 from TSPlib. Report the outcomes after 5000, 10000, and 20000 generations. To clarify: these are 3*4*10=120 runs, i.e., 3 algorithms X 4 population sizes X 10 instances. 
• (Experiment 2) From these three algorithms, run your best algorithm with a population size of 50 for 10000 generations on the ten TSPlib instances mentioned above. Report for each instance either (1) the average cost and the standard deviation or (2) the median cost and the interquartile range.
### Notes: 
• For the large instance, e.g., PR2392: if you cannot ﬁnish a single run, please report the results that you can achieve within some time limit, e.g., ”after 4 hours” or ”after 8 hours”. 
• How often you repeat the experiment involving your best algorithm is up to you. 10 repetitions is a good start, 30 or 100 repetitions will result in more reliable means/medians, however, you might not have the time to run the experiments that often. 
• How to report the outcomes: for each of Experiment 1 and Experiment 2, submit the results in a plain text ﬁle (no Excel spreadsheet or similar). This means that you will have to submit in total two text ﬁles for this Exercise.
It is absolutely critical that you provide detailed instructions on how to reproduce the results. With this, we mean that the TAs have to be able to run your code and get results that are somewhat similar to what you are reporting.


