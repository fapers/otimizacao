# MODELAGEM
# Variáveis x e y
# Função objetivo: maximixar a área x*y
# Restrições: 2x + y <= 100

import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def f(x):
    pen = 0
    if not 2*x[0] + x[1] <= 100: pen = np.inf
    
    return -(x[0] * x[1] - pen)

varbounds = np.array([[0,50], [0,100]]) 
vartype = np.array([['real'], ['real']])

model=ga(function=f,\
            dimension=2,\
            variable_type_mixed=vartype,\
            variable_boundaries=varbounds)

model.run()
