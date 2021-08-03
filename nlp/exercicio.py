import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import time, numpy as np

# Modelo
model = pyo.ConcreteModel()

# Variáveis
model.x = pyo.Var(initialize=0, bounds=(-5,5))
model.y = pyo.Var(initialize=0, bounds=(-5,5))
x = model.x
y = model.y

# Restrições
# Sem restrições

# Função objetivo
model.obj = pyo.Objective(expr= pyo.cos(x+1) + pyo.cos(x) * pyo.cos(y), sense=maximize)

begin = time.time()
opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')
# opt = SolverFactory('scip', executable='C:\\SCIPOptSuite7\\bin\\scip.exe')
opt.options['tol']=1e-6
opt.solve(model)
end = time.time() - begin

# model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

# Impressão
print(f'Tempo = {np.round(end, 2)}')
print(f'x= {x_value}')
print(f'y= {y_value}')