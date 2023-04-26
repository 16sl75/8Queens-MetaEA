import random
import meta_initialization_RL
def permutation_swap (individual):
    """Mutate a permutation"""
    
    swap_individual=meta_initialization_RL.meta_permutation(meta_popsize=1)
    mutant = individual.copy()
    

    select=random.sample(range(len(individual)-1),2)
   
    i=select[0]
    j=select[1]#get two random  allele
  

    mutant[i],mutant[j]=swap_individual[0][i],swap_individual[0][j]

    return mutant
