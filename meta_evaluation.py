"""

A genetic algorithm for the eight queens puzzle

Colleciton of mutation methods

"""

import random
import numpy
import datetime
from functools import reduce
import matplotlib
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot

# import your own modules
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection

# Design calls parameters using pipes
def pipeline(num, *args):
    '''
    To make more standardized we can use a list to store the hyperparameter function:
    purpose: stores each function which might be called;
    '''
    func_list = [parent_selection.MPS, parent_selection.tournament, parent_selection.random_uniform,
                 recombination.permutation_cut_and_crossfill, survivor_selection.mu_plus_lambda, 
                 survivor_selection.replacement, survivor_selection.random_uniform, meta_evaluation]

    '''Define a function that takes a number as input 
       returns the corresponding hyperargument function'''
    def get_func_by_index(index):
        return func_list[index] 
    
    '''Using the pipeline pattern to combine functions,
       the output of each function is used as input to the next function'''
    func = get_func_by_index(num)
    # result = reduce(lambda x, f: f(x), [args, func]) # type: ignore
    #reference: https://blog.csdn.net/qq_47183158/article/details/116598952
    result = func(*args)
    return result
    
def visualization_queens(answer, string_length):
    x = []
    y = []
    for i in range(string_length):
        y.append(answer[i] - 0.5)  # y=[i.index(1)+0.5, i.index(2)+0.5, i.index(3)+0.5, i.index(4)+0.5, i.index(5)+0.5, i.index(6)+0.5, i.index(7)+0.5, i.index(8)+0.5]
        x.append(i + 0.5)
    # print("y=", y, "x=", x)
    matplotlib.pyplot.title("Using Genetic Algorithm to Solve " + str(string_length) + "-Queens' Problem")
    matplotlib.pyplot.axis([0, string_length, 0, string_length])
    matplotlib.pyplot.grid()
    matplotlib.pyplot.plot(x, y, '*')

    x_major_locator = MultipleLocator(1)

    y_major_locator = MultipleLocator(1)

    ax = matplotlib.pyplot.gca()

    ax.xaxis.set_major_locator(x_major_locator)
    
    ax.yaxis.set_major_locator(y_major_locator)
    
    matplotlib.pyplot.xlim(-0.0, string_length)

    matplotlib.pyplot.ylim(-0.0, string_length)

    matplotlib.pyplot.show()
    matplotlib.pyplot.show()

# set some Default values of each parameter, can be changed when it is called
def meta_evaluation(meta_individual):
    # (popsize = 200, tournament_size = 8, xover_rate = 0.6,
    # mut_rate = 0.3, gen_limit = 50, string_length = 6,
    # parent_selection_method = 'MPS',
    # survivor_selection_method = 'mu_plus_lambda')
    '''
    There are some parameters that can be set:
    --------
    "popsize": the size of the population
    "tournament_size": the size of the tournament
    "xover_rate": the crossover rate
    "mut_rate": the mutation rate
    "gen_limit": the generation limit
    "string_length": the length of the string
    "parent_selection_method": the method of parent selection, you can choose from 'MPS', 'tournament', 'random_uniform'
    "survivor_selection_method": the method of survivor selection, you can choose from 'mu_plus_lambda', 'replacement', 'random_uniform'
    ---------
    '''
    
    popsize, tournament_size, xover_rate, mut_rate = meta_individual[0], meta_individual[1], meta_individual[2], \
                                                     meta_individual[3]
    gen_limit, string_length, parent_selection_method, survivor_selection_method = meta_individual[4], meta_individual[
        5], meta_individual[6], meta_individual[7]

    ''' 1. initialize the random number generator, and print the current time  ''' 
    random.seed()
    numpy.random.seed()
    matplotlib.pyplot.clf()
    time_start = datetime.datetime.now()
    time_current = time_start
    print("Evaluation Begins at: ",time_current.strftime('%Y-%m-%d %H:%M:%S'))

    ''' 2. set some Built-in parameters '''
    n = 0
    success_count = 0   # count the number of solution in a generation that results in maximum fitness
    Success_queens = []  # store the success queens
    mating_pool_size = int(int(popsize)*0.5)  # the size of the mating pool
    number_of_success_queens_found = 0  # count the number of success queens
    Max_turn = int(string_length)**3  # define the maximum number of rounds = string_length**3
    parent_selection_dict = {'MPS': 0, 'tournament': 1, 'random_uniform': 2}
    survivor_selection_dict = {'mu_plus_lambda': 4, 'replacement': 5, 'random_uniform': 6}
    survivor_selection = survivor_selection_dict[survivor_selection_method]
    parent_selection = parent_selection_dict[parent_selection_method]
    
    ''' 3. Evolution begins '''
    while n < Max_turn:
        
        # 3.1 Initialize the population
        gen = 0 
        fitness = []
        population = initialization.permutation(popsize, string_length)
        for i in range (0, popsize):
            fitness.append(evaluation.fitness_8queen(population[i]))
        '''
        if n % 20 == 0:
            # print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness)/len(fitness), "Round", n)
            print("Another 20 turns started!","Now at , n = ", n, " turn. ")
        '''
        if (string_length == 4 and number_of_success_queens_found == 2) or (string_length == 5 and number_of_success_queens_found == 10) or (string_length == 6 and number_of_success_queens_found == 4) or (string_length == 7 and number_of_success_queens_found == 40) or (string_length == 8 and number_of_success_queens_found == 92) or (string_length == 9 and number_of_success_queens_found == 352) or (string_length == 10 and number_of_success_queens_found == 724):
            break
        
        # 3.2 Evolution process
        while gen < gen_limit:
            if parent_selection == 0:
                parents_index = pipeline(0, fitness, mating_pool_size)
            elif parent_selection == 1:
                parents_index = pipeline(1, fitness, mating_pool_size, tournament_size)
            else:
                parents_index = pipeline(2, popsize, mating_pool_size)
            random.shuffle(parents_index)  # type: ignore
            
            # reproduction
            offspring =[]
            offspring_fitness = []
            
            i= 0 # initialize the counter for parents in the mating pool
            # offspring are generated using selected parents in the mating pool
            while len(offspring) < mating_pool_size:
                # recombination
                if random.random() < xover_rate:
                    off1,off2 = pipeline(3, population[parents_index[i]], population[parents_index[i+1]])
                else:
                    off1 = population[parents_index[i]].copy()
                    off2 = population[parents_index[i+1]].copy()

                # mutation
                if random.random() < mut_rate:
                    off1 = mutation.permutation_swap(off1)
                if random.random() < mut_rate:
                    off2 = mutation.permutation_swap(off2)

                offspring.append(off1)
                offspring_fitness.append(evaluation.fitness_8queen(off1))
                offspring.append(off2)
                offspring_fitness.append(evaluation.fitness_8queen(off2))
                i = i + 2 

            # organize the population of next generation
            
            if survivor_selection == 4:
                population, fitness =  pipeline(4, population, fitness, offspring, offspring_fitness)
            elif survivor_selection == 5:
                population, fitness =  pipeline(5, population, fitness, offspring, offspring_fitness)
            else:
                population, fitness = pipeline(6, population, fitness, offspring, offspring_fitness)
            gen = gen + 1  # update the generation counter

        # evolution ends
        if max(fitness) == 0.5*string_length*(string_length-1):
            success_count = success_count + 1
        # print the final best solution(s)
        k = 0
        answer = []
        for i in range(0, popsize):
            if fitness[i] == 0.5 * string_length * (string_length - 1) and population[i] not in Success_queens: # if fitness[i] == max(fitness):
                number_of_success_queens_found = number_of_success_queens_found + 1
                #print("best solution", k, population[i], fitness[i], ",number_of_success_queens_found =", number_of_success_queens_found, ",n=", n)
                k = k+1
                answer = population[i]
                Success_queens.append(answer)
                # print("answer=", answer)

                # 可行解的可视化
                #visualization_queens(answer, string_length)

        # print("number of queens = ", str(string_length), ",number_of_success_queens_found =", number_of_success_queens_found,",n=", n)
        n = n + 1
    '''
    for queen in Success_queens:
        print("best Quuens = ",queen)
    print("success count = ", success_count, "out of number of tries = ", str(n), "Success rate =", str(success_count/n*100)+"%")
    print("number of queens = ", str(string_length), "number_of_success_queens_found =", number_of_success_queens_found)
    # input("Please enter any key to continue......")
    print("popsize =", popsize, "gen_limit =" , gen_limit)
    '''
    task_name = "Evaluation "
    time_prev = time_current
    time_current = datetime.datetime.now()
    print(task_name + "Ends at:", time_current)
    run_time_1 = (time_current - time_prev).seconds; run_time_2 = (time_current - time_start).seconds
    hour = run_time_1//3600; minute = (run_time_1-3600*hour)//60; second = run_time_1-3600*hour-60*minute
    print (f'{task_name} takes : {hour}Hours: {minute}Minutes: {second}Seconds')
    hour = run_time_2//3600; minute = (run_time_2-3600*hour)//60; second = run_time_2-3600*hour-60*minute
    print (f'Time from start  : {hour}Hours: {minute}Minutes: {second}Seconds')
    """Data_Prep ends."""
    time_taken = time_current - time_prev
    time_taken_in_microseconds = time_taken.seconds + time_taken.microseconds/1000000
    print("Time taken = ",time_taken_in_microseconds , " s")


    meta_fitness = [success_count/n, time_taken_in_microseconds, number_of_success_queens_found]
    return meta_fitness



