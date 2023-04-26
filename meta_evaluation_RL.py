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
from test_carpole import carpole
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
    


# set some Default values of each parameter, can be changed when it is called
def meta_evaluation(meta_individual):
    gamma, learning_rate, episodes, epsilon, buffer_len, batch_size = meta_individual[0], meta_individual[1], meta_individual[2], \
                                                     meta_individual[3], meta_individual[4], meta_individual[5]
    
    
    ''' 1. initialize the random number generator, and print the current time  ''' 
    random.seed()
    numpy.random.seed()
    
    time_start = datetime.datetime.now()
    time_current = time_start
    print("Evaluation Begins at: ",time_current.strftime('%Y-%m-%d %H:%M:%S'))

    score = carpole(gamma=gamma, learning_rate=learning_rate, episodes=episodes, epsilon=epsilon, buffer_len=buffer_len, batch_size=batch_size)
    
    
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
    print("The fitness for current individual is:", int(score))

    meta_fitness = [int(score)]
    return meta_fitness



