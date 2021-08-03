import numpy as np
from geneticalgorithm import geneticalgorithm as ga


# pip install geneticalgorithm
# https://pypi.org/project/geneticalgorithm/

def f(x):
    pen = 0
    if not -x[0]+2*x[1]*x[0] <= 8: pen = np.inf
    if not 2*x[0]+x[1] <= 14: pen = np.inf
    if not 2*x[0]-x[1]<=10:pen=np.inf
    
    if x[0]>10: return x[0]+x[1]
    else: return -(x[0]+x[1]*x[0]) + pen

varbounds = np.array([[0,10],[0,10]])
vartype = np.array([['int'], ['real']])

algorithm_param = {'max_num_iteration': 1000,\
                   'population_size':100,\
                   'mutation_probability':0.9,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 1,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

model=ga(function=f,\
            dimension=2,\
            variable_type_mixed=vartype,\
            variable_boundaries=varbounds,\
            algorithm_parameters=algorithm_param)

model.run()
