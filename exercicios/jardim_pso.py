# MODELAGEM
# Variáveis x e y
# Função objetivo: maximixar a área x*y
# Restrições: 2x + y <= 100

import numpy as np
from numpy.random.mtrand import f
from pyswarm import pso

def model_obj(x):
    pen = 0
    x[0] = np.round(x[0], 0)
    if not 2*x[0] + x[1] <= 100: pen = np.inf
    return -(x[0]*x[1]) + pen

def cons(x):
    return []

lb = [0,0]
ub = [100,100]
x0 = [0,0]

xopt, fopt = pso(model_obj, lb, ub, x0, cons)

print(f'x = {xopt[0]}')
print(f'y = {xopt[1]}')
