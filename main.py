
import random
import numpy


# import your own modules
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection
import matplotlib
from matplotlib.ticker import MultipleLocator
from matplotlib import pyplot

   
def main():
   
    random.seed()
    numpy.random.seed()

    string_length = 8  # may extend to N queens
    # you may test on different parameter settings
    popsize = 20  
    mating_pool_size = int(popsize*0.5) # has to be even
    tournament_size = 4
    xover_rate = 0.9
    mut_rate = 0.2
    gen_limit = 50
    Success_queens = []
    success_count = 0 #count the number of solution in a generation that results in maximum fitness
    n = 0
    Max_turn = 300
    while n < Max_turn:
        # initialize population
        gen = 0 # initialize the generation counter
        population = initialization.permutation(popsize, string_length)
        fitness = []
        for i in range (0, popsize):
            fitness.append(evaluation.fitness_8queen(population[i]))
        #print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness)/len(fitness))

        # evolution begins
        while gen < gen_limit:

            # pick parents
            parents_index = parent_selection.MPS(fitness, mating_pool_size)
            # parents_index = parent_selection.tournament(fitness, mating_pool_size, tournament_size)
            # parents_index = parent_selection.random_uniform(popsize, mating_pool_size)

            # in order to randomly pair up parents
            random.shuffle(parents_index)

            # reproduction
            offspring =[]
            offspring_fitness = []
            i= 0 # initialize the counter for parents in the mating pool

            # offspring are generated using selected parents in the mating pool
            while len(offspring) < mating_pool_size:

                # recombination
                if random.random() < xover_rate:
                    off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
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
                i = i+2  # update the counter

            # organize the population of next generation
            population, fitness = survivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
    #        population, fitness = survivor_selection.replacement(population, fitness, offspring, offspring_fitness)
    #        population, fitness = survivor_selection.random_uniform(population, fitness, offspring, offspring_fitness)

            gen = gen + 1  # update the generation counter
            #print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))

        # evolution ends
        k=1
        if max(fitness) == 0.5 * string_length * (string_length - 1):
            success_count = success_count + 1
            for i in range(0, popsize):
                if fitness[i] == max(fitness) and (population[i] not in Success_queens):
                    #print("best solution", k, population[i], fitness[i])
                    Success_queens.append(population[i])
                    k = k + 1
        # print the final best solution(s)
        """k = 0
        for i in range (0, popsize):
            if fitness[i] == max(fitness):
                print("best solution", k, population[i], fitness[i])
                k = k+1"""

        n = n + 1
        '''
    for i in range(0, len(Success_queens)):
        print("best QUeens = ",Success_queens[i])
        # 可行解的可视化
        x = []
        y = []
        answer = Success_queens[i]
        for i in range(string_length):
            y.append(answer[i]-0.5)  # y=[i.index(1)+0.5, i.index(2)+0.5, i.index(3)+0.5, i.index(4)+0.5, i.index(5)+0.5, i.index(6)+0.5, i.index(7)+0.5, i.index(8)+0.5]
            x.append(i + 0.5)
        # print("y=", y, "x=", x)
        matplotlib.pyplot.title("Using Genetic Algorithm to Solve " + str(string_length) + "-Queens' Problem")
        matplotlib.pyplot.axis([0, string_length, 0, string_length])
        matplotlib.pyplot.grid()
        matplotlib.pyplot.plot(x, y, '*')
        # Matplotlib设置横纵坐标刻度, https://blog.csdn.net/weixin_45422335/article/details/108368170
        x_major_locator = MultipleLocator(1)
        # 把x轴的刻度间隔设置为1，并存在变量里
        y_major_locator = MultipleLocator(1)
        # 把y轴的刻度间隔设置为10，并存在变量里
        ax = matplotlib.pyplot.gca()
        # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(x_major_locator)
        # 把x轴的主刻度设置为1的倍数
        ax.yaxis.set_major_locator(y_major_locator)
        # 把y轴的主刻度设置为10的倍数
        matplotlib.pyplot.xlim(-0.0, string_length)
        # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
        matplotlib.pyplot.ylim(-0.0, string_length)
        # 把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
        matplotlib.pyplot.show()
        matplotlib.pyplot.show()
        '''

    #print("\nsuccess_count=",success_count,"Max_turn=",Max_turn, "Success rate = ",success_count/Max_turn)
    #print("\nThe total number of success queens found = ",len(Success_queens))

# end of main


main()





