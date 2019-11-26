import numpy as np
import pandas as pd
#these are the necessary python libraries.

def bootstrap_replicate(data, function):
    return function(np.random.choice(data, size=len(data)))
    #this is the function for creating a bootstrap replicate.

def draw_bootstrap_replicates(data, func, size = 1):
    
    bs_replicates = np.empty(shape = size)
    #this initializes an array of bootstrap replicates.
    
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate(data, func)
    #this generates the bootstrap replicates.
        
    return bs_replicates
    
if __name__ == '__main__':
    #this is the mainguard. The mainguard contains work particular to my project and allows just the bs_replicates function 
    #to be imported by other users 
    
    df = pd.read_csv("gandhi_et_al_bouts.csv")
    #import the data. this data was modified beforehand in a spreadsheet for coding purposes.
    
    bout_length_wt = np.array(df[df.genotype == 'wt'].bout_length)
    bout_length_mut = np.array(df[df.genotype == 'mut'].bout_length)
    #selecting data from our dataframe.
    
    mean_wt = np.mean(bout_length_wt)
    mean_mut = np.mean(bout_length_mut)
    #calculate means of data.
    
    bs_reps_wt = draw_bootstrap_replicates(bout_length_wt, np.mean, size = 10000)
    bs_reps_mut = draw_bootstrap_replicates(bout_length_mut, np.mean, size = 10000)
    #this draws 10,000 bootstrap replicates from the wild-type and mutant-type bout lengths.
    
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
    #this is to calculate the 95% confidence interval for the boostrap replicates.

    conf_int_wt = [round(conf_int_wt[i], 2) for i in range(len(conf_int_wt))]
    conf_int_mut = [round(conf_int_mut[i], 2) for i in range(len(conf_int_mut))]
    #this is to round the results to two decimal places, so that it is more readable.
    
    print("Wild-type mean bout length: " + str(round(mean_wt, 2)) + " with confidence interval " + str(conf_int_wt))
    print("Mutant-type mean bout length: " + str(round(mean_mut, 2)) + " with confidence interval " + str(conf_int_mut))
    #prints readable results.
