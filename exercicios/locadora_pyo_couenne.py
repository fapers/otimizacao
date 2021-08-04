# variáveis: p: valor de aluguel
# Função objetivo: Max p * N
# Restrições: N(p) = 1001-5*p; 50 <= p <= 200; N é inteiro

import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Definição
model = pyo.ConcreteModel()
model.p = pyo.Var(bounds=(50,200))
model.n = pyo.Var(within=Integers, bounds=(0,1001))
p = model.p
n = model.n

# Função objetivo
model.obj = pyo.Objective(expr= p*n, sense=maximize)

# Restrições
model.c3 = pyo.Constraint(expr=n == 1001 - 5*p)


opt = SolverFactory('couenne', executable='C:\\couenne\\bin\\couenne.exe')
opt.solve(model)

print(f'p: {pyo.value(p):.2f}')
print(f'N: {pyo.value(n):.2f}')
print(f'FO: {pyo.value(p)*pyo.value(n):.2f}')
