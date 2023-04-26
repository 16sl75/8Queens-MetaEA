import meta_evaluation; import meta_initialization; import random; import meta_mutation
import meta_parent_selection; import meta_recombination; import meta_survivor_selection
import Meta_Utility
import json
import numpy as np
def meta_main():
    """Meta EA Begins"""
    """INITIALISE population with random candidate solutions"""
    meta_popsize = 8; string_length = 8
    meta_population = meta_initialization.meta_permutation(meta_popsize, string_length)

    """EVALUATE each candidate"""
    meta_fitness_list = []
    for meta_individual in meta_population:
        print("\n\nindividual=", meta_individual)
        meta_fitness = meta_evaluation.meta_evaluation(meta_individual) # you can change the parameters here
        print("meta_fitness[success_rate, time_taken, number_of_success_queens_found]=", meta_fitness)
        print(f'popsize:{meta_individual[0]}, tournament_size:{meta_individual[1]}, xover_rate:{meta_individual[2]}, mut_rate:{meta_individual[3]}')
        print(f'gen_limit:{meta_individual[4]}, string_length:{meta_individual[5]}, parent_selection_method:{meta_individual[6]}, survivor_selection_method:{meta_individual[7]}')
        meta_fitness_list.append(meta_fitness)
    """
    REPEAT UNTIL (TERMINATION CONDITION is satisfied) DO  
        1 SELECT parents; 
        2 RECOMBINE pairs of parents; 
        3 MUTATE the resulting offsprings  
        4 EVALUATE new candidates; 
        5 SELECT individuals for the next generation; 
    """
    print("\n\nMeta main summary:")
    
    meta_sorted_fitness_list, meta_sorted_population, arrSortedIndex = Meta_Utility.arraySort(meta_fitness_list, meta_population)
    print("meta_sorted_fitness_list=\n", meta_sorted_fitness_list)
    print("meta_sorted_population=\n", meta_sorted_population)
    print("arrSortedIndex=\n", arrSortedIndex)
    


    meta_gen_limit = 50; meta_mating_pool_size = int(meta_popsize/2); meta_xover_rate = 0.5; meta_gen = 0
    average_fitness = []
    average_queen = []
    meta_sorted_fitness_history = []
    propmax = 0.7
    propmin = 0.3
    
    while meta_gen < meta_gen_limit:

        # 1 SELECT parents;
        # pick parents
        meta_mut_rate = 1.0 - np.random.rand()**(1.0-meta_gen/meta_gen_limit)
      
     
        meta_parents_index = meta_parent_selection.meta_tournament(meta_fitness_list, meta_mating_pool_size, 4)
        #meta_parents_index = meta_parent_selection.meta_MPS(meta_fitness_list, meta_mating_pool_size)
        # in order to randomly pair up parents
        random.shuffle(meta_parents_index)
        # offspring are generated using selected parents in the mating pool

        # 2 RECOMBINE pairs of parents;
        # 3 MUTATE the resulting offsprings
        # 4 EVALUATE new candidates;
        meta_offspring =[]
        meta_offspring_fitness = []
        ip= 0 # initialize the counter for parents in the mating pool

        queen_found = [meta_fitness_list[i][2] for i in range(len(meta_fitness_list))]
        fmax1 = max(queen_found)
        favg1 = sum(queen_found)/len(queen_found)
        
        
        while len(meta_offspring) < meta_mating_pool_size:
            
            # 2 RECOMBINE pairs of parents;
            
            
            # adaptive crossoverrate
            fitness_check1 = max(queen_found[ip], queen_found[ip+1])
            if fitness_check1 < favg1:
                meta_xover_rate = propmax
            elif fmax1 != favg1:
                meta_xover_rate = propmax - (propmax-propmin)*((fitness_check1-favg1)/(fmax1-favg1))
            else:
                time_taken = [meta_fitness_list[i][1] for i in range(len(meta_fitness_list))]
                fmin2 = min(time_taken)
                favg2 = sum(time_taken)/len(time_taken)
                fitness_check2 = min(time_taken[ip], time_taken[ip+1])
                if (favg2-fmin2)/fmin2 < 0.1:
                    success_rate = [meta_fitness_list[i][0] for i in range(len(meta_fitness_list))]
                    fmax3 = max(success_rate)
                    favg3 = sum(success_rate)/len(success_rate)
                    fitness_check3 = max(success_rate[ip], success_rate[ip+1])
                    if fitness_check3 < favg3:
                        meta_xover_rate = propmax
                    elif fmax3 != favg3:
                        meta_xover_rate = propmax - (propmax-propmin)*((fitness_check3-favg3)/(fmax3-favg3))
                    else:
                        meta_xover_rate = propmin
                elif fitness_check2 > favg2:
                    meta_xover_rate = propmax
                else:
                    meta_xover_rate = propmax - (propmax-propmin)*((favg2 - fitness_check2)/(favg2 - fmin2))

            # recombination
            
            if random.random() < meta_xover_rate:
                off1,off2 = meta_recombination.permutation_cut_and_crossfill(meta_population[meta_parents_index[ip]], meta_population[meta_parents_index[ip+1]])
            else:
                off1 = meta_population[meta_parents_index[ip]].copy()
                off2 = meta_population[meta_parents_index[ip+1]].copy()
            # 3 MUTATE the resulting offsprings
            
            
            # mutation
            if random.random() < meta_mut_rate:
                off1 = meta_mutation.permutation_swap(off1)
            if random.random() < meta_mut_rate:
                off2 = meta_mutation.permutation_swap(off2)
            
            # 4 EVALUATE new candidates;
            meta_offspring.append(off1)
            meta_offspring_fitness.append(meta_evaluation.meta_evaluation(off1))
            meta_offspring.append(off2)
            meta_offspring_fitness.append(meta_evaluation.meta_evaluation(off2))
            ip += 2

        # 5 SELECT individuals for the next generation;
        meta_population, meta_fitness_list = meta_survivor_selection.meta_mu_plus_lambda(meta_population, meta_fitness_list, meta_offspring, meta_offspring_fitness)
        #meta_population, meta_fitness_list = meta_survivor_selection.meta_replacement(meta_population, meta_fitness_list, meta_offspring, meta_offspring_fitness)

        fitness_acc = [meta_fitness_list[i][0] for i in range(len(meta_fitness_list))]
        queen_found = [meta_fitness_list[i][2] for i in range(len(meta_fitness_list))]
        average_fitness.append(sum(fitness_acc)/len(fitness_acc))
        average_queen.append(sum(queen_found)/len(queen_found))
        print("The average fitness in this generation is:", average_fitness[-1])
        print("The average qualified solutions in theis generation is:", average_queen[-1])
        print(f"\n\nMeta main summary at meta_generation of {meta_gen}: ")
        meta_sorted_fitness_list, meta_sorted_population, arrSortedIndex = Meta_Utility.arraySort(meta_fitness_list,meta_population)
        # for i in range(len(meta_sorted_fitness_list)):
        #     print("meta_fitness[success_rate, time_taken, number_of_success_queens_found]=",[meta_sorted_fitness_list[i][0], meta_sorted_fitness_list[i][1], meta_sorted_fitness_list[i][2]])
        #     print(f'popsize:{meta_sorted_population[i][0]}, tournament_size:{meta_sorted_population[i][1]}, xover_rate:{meta_sorted_population[i][2]}, mut_rate:{meta_sorted_population[i][3]}')
        #     print(f'gen_limit:{meta_sorted_population[i][4]}, string_length:{meta_sorted_population[i][5]}, parent_selection_method:{meta_sorted_population[i][6]}, survivor_selection_method:{meta_sorted_population[i][7]}')
        print("\nmeta_fitness[success_rate, time_taken, number_of_success_queens_found]=\n", meta_sorted_fitness_list)
        print("meta_population = \n", meta_sorted_population)
        meta_sorted_fitness_history.append(meta_sorted_fitness_list)
        meta_gen = meta_gen + 1
       
        
    # Store and plot the result

    json_object = json.dumps(average_fitness, indent=4)
    with open("result_fitness.json", "w") as outfile:
        outfile.write(json_object)

    json_object = json.dumps(average_queen, indent=4)
    with open("result_queens.json", "w") as outfile:
        outfile.write(json_object)
        
    print("\n\nMeta main summary at end: ")
    meta_sorted_fitness_list, meta_sorted_population, arrSortedIndex = Meta_Utility.arraySort(meta_fitness_list,meta_population)
    # for i in range(len(meta_sorted_fitness_list)):
    #     print("meta_fitness[success_rate, time_taken, number_of_success_queens_found]=", [meta_sorted_fitness_list[i][0],meta_sorted_fitness_list[i][1],meta_sorted_fitness_list[i][2]])
    #     print( f'popsize:{meta_sorted_population[i][0]}, tournament_size:{meta_sorted_population[i][1]}, xover_rate:{meta_sorted_population[i][2]}, mut_rate:{meta_sorted_population[i][3]}')
    #     print(f'gen_limit:{meta_sorted_population[i][4]}, string_length:{meta_sorted_population[i][5]}, parent_selection_method:{meta_sorted_population[i][6]}, survivor_selection_method:{meta_sorted_population[i][7]}')
    print("\nmeta_fitness[success_rate, time_taken, number_of_success_queens_found]=\n",meta_sorted_fitness_list)
    print("meta_population = \n", meta_sorted_population)
    print(f"meta_sorted_fitness_history = \n{meta_sorted_fitness_history}")
    best_chroma_successRate_history = []
    best_chroma_timeTaken_history = []
    best_chroma_queensFound_history = []
    worst_chroma_successRate_history = []
    worst_chroma_timeTaken_history = []
    worst_chroma_queensFound_history = []
    for data in meta_sorted_fitness_history:
        best_chroma_successRate_history.append(data[0][0])
        best_chroma_timeTaken_history.append(data[0][1])
        best_chroma_queensFound_history.append(data[0][2])
        worst_chroma_successRate_history.append(data[-1][0])
        worst_chroma_timeTaken_history.append(data[-1][1])
        worst_chroma_queensFound_history.append(data[-1][2])

    Meta_Utility.plot_2_curves(curve_1=best_chroma_successRate_history, curve_2=worst_chroma_successRate_history, legend_1="best_chroma_successRate_history", legend_2="worst_chroma_successRate_history", pic_title="Success Rate against Meta Generation", xLabel ="Meta Generation", yLabel = "Success Rate", y_major_locator_=0.5)
    Meta_Utility.plot_2_curves(curve_1=best_chroma_timeTaken_history, curve_2=worst_chroma_timeTaken_history, legend_1="best_chroma_timeTaken_history", legend_2="worst_chroma_timeTaken_history", pic_title="Time Taken against Meta Generation", xLabel ="Meta Generation", yLabel = "Time Taken", y_major_locator_=5)
    Meta_Utility.plot_2_curves(curve_1=best_chroma_queensFound_history, curve_2=worst_chroma_queensFound_history, legend_1="best_chroma_queensFound_history", legend_2="worst_chroma_queensFound_history", pic_title="Queens Found against Meta Generation", xLabel ="Meta Generation", yLabel = "Queens Found", y_major_locator_=5)
    Meta_Utility.plot_1_curves(curve_1=best_chroma_timeTaken_history, legend_1="best_chroma_timeTaken_history", pic_title="Best Chrome Time Taken(s) against Meta_Generation", xLabel="Meta_Generation", yLabel="Time Taken(s)", y_major_locator_=5)
    Meta_Utility.plot_1_curves(curve_1=worst_chroma_timeTaken_history, legend_1="worst_chroma_timeTaken_history", pic_title="Worst Chrome Time Taken(s) against Meta_Generation", xLabel="Meta_Generation", yLabel="Time Taken(s)", y_major_locator_=0.1)

meta_main()