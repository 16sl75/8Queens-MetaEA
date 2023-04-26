import random
import meta_initialization
def permutation_swap (individual):
    """Mutate a permutation"""
    
    swap_individual=meta_initialization.meta_permutation(meta_popsize=1, string_length=individual[5])
    mutant = individual.copy()
    
    # student code starts
    select=random.sample(range(len(individual)-1),2)
   
    i=select[0]
    j=select[1]#get two random  allele
  

    mutant[i],mutant[j]=swap_individual[0][i],swap_individual[0][j]
    # student code ends
    #print("offspringlength")
    #print(len(mutant))
    return mutant
