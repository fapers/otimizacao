import pyomo.environ as pyo
import numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory
import time

model = pyo.ConcreteModel()

# Variáveis de definição
model.x = pyo.Var(bounds=(-np.inf,3))
model.y = pyo.Var(bounds=(0,np.inf))
x = model.x
y = model.y

# Restrições
model.C1 = pyo.Constraint(expr=x+y<=8)
model.C2 = pyo.Constraint(expr=8*x+3*y>=-24)
model.C3 = pyo.Constraint(expr=-6*x+8*y<=48)
model.C4 = pyo.Constraint(expr=3*x+5*y<=15)

# Função Objetivo
model.obj = pyo.Objective(expr=-4*x-2*y, sense=minimize)

# Solução
ini = time.time()
opt = SolverFactory('glpk', executable='C:\\glpk-4.65\\w64\\glpsol.exe')
opt.solve(model)
fim = time.time()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)
print("Tempo: ", fim-ini)
