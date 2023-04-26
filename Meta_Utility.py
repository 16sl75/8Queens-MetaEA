import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

def arraySort(meta_fitness_list, meta_population):
    # print("\n\nMeta main summary")
    meta_fitness_population_pair = []
    for i in range(len(meta_fitness_list)):
        # print("meta_fitness[success_rate, time_taken, number_of_success_queens_found]=", [meta_fitness_list[i][0],meta_fitness_list[i][1],meta_fitness_list[i][2]])
        # print( f'[popsize:{meta_population[i][0]}, tournament_size:{meta_population[i][1]}, xover_rate:{meta_population[i][2]}, mut_rate:{meta_population[i][3]}')
        # print(f'gen_limit:{meta_population[i][4]}, string_length:{meta_population[i][5]}, parent_selection_method:{meta_population[i][6]}, survivor_selection_method:{meta_population[i][7]}]')
        meta_fitness_population_pair.append([meta_fitness_list[i][0], meta_fitness_list[i][1], meta_fitness_list[i][2], meta_population[i]])
    # print("\nmeta_fitness[success_rate, time_taken, number_of_success_queens_found]=\n",meta_fitness_list)
    # print("meta_population = \n", meta_population)
    # print("meta_fitness_population_pair = \n", meta_fitness_population_pair)
    arr = np.array(meta_fitness_population_pair, dtype=object)
    # print("arr = \n", arr)
    arrSortedIndex = np.lexsort(((-1)*arr[:, 0], arr[:, 1], (-1)*arr[:, 2]))
    # print("arrSortedIndex =", arrSortedIndex)
    # print('%===== 按照z优先(降序)，y次级(升序)，x最后(降序)规则排序后 ======')
    # print(arr[arrSortedIndex, :])
    meta_sorted_fitness_list = []
    meta_sorted_population = []
    for index in arrSortedIndex:
        A = [meta_fitness_list[index][0], meta_fitness_list[index][1], meta_fitness_list[index][2]]
        B = meta_population[index]
        # print(A)
        # print(B)
        meta_sorted_fitness_list.append(A)
        meta_sorted_population.append(B)
    return meta_sorted_fitness_list, meta_sorted_population, arrSortedIndex

def indexSort(meta_fitness_list):

    arr = np.array(meta_fitness_list, dtype=object)

    arrSortedIndex = np.lexsort(((-1)*arr[:, 0], arr[:, 1], (-1)*arr[:, 2]))
    
    return arrSortedIndex


def fitnessSort(meta_fitness_list):
    arr = np.array(meta_fitness_list, dtype=object)

    arrSortedIndex = np.lexsort(((-1)*arr[:, 0], arr[:, 1], (-1)*arr[:, 2]))

    meta_sorted_fitness_list = []
    for index in arrSortedIndex:
        A = [meta_fitness_list[index][0], meta_fitness_list[index][1], meta_fitness_list[index][2]]
        meta_sorted_fitness_list.append(A)

    return meta_sorted_fitness_list

def plot_2_curves(curve_1,curve_2,legend_1, legend_2, pic_title, xLabel, yLabel, y_major_locator_=1):
    plt.title(pic_title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.axis([0,len(curve_1),0,max(max(curve_1),max(curve_2))*1.3])
    x_major_locator=MultipleLocator(5)
    y_major_locator=MultipleLocator(y_major_locator_)
    plt.ylim(0,max(max(curve_1),max(curve_2))*1.2)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    line1, = plt.plot(curve_1, "r:.") # line1, = plt.plot(curve_1, "r:o")
    line2, = plt.plot(curve_2, "g:.") # line2, = plt.plot(curve_2, "g:d")
    plt.legend([line1,line2],[legend_1, legend_2], loc="upper right")
    plt.grid(True)
    plt.show()

def plot_1_curves(curve_1, legend_1, pic_title, xLabel, yLabel, y_major_locator_=1):
    plt.title(pic_title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    # plt.axis([-0.2,len(curve_1),-0.2, max(curve_1)*1.2])
    x_major_locator=MultipleLocator(5)
    # y_major_locator=MultipleLocator(y_major_locator_)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    # ax.yaxis.set_major_locator(y_major_locator)
    plt.ylim(0,max(curve_1)*1.2)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    line1, = plt.plot(curve_1, "r:.") # line1, = plt.plot(curve_1, "r:o")
    plt.legend([line1],[legend_1], loc="upper right")# "upper right"
    plt.grid(True)
    plt.show()