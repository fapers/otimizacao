from sys import executable
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,None))
model.y = pyo.Var(bounds=(0,None))
x = model.x
y = model.y

model.obj = pyo.Objective(expr= x*y, sense=maximize)
model.c1 = pyo.Constraint(expr=2*x+y <= 100)

opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')
opt.solve(model)

print(f'x: {pyo.value(x):.2f}')
print(f'y: {pyo.value(y):.2f}')
print(f'A: {pyo.value(x)*pyo.value(y):.2f}')
