from pyomo.core.expr.current import Mode
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr= -x+2*y<=8)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

model.obj = pyo.Objective(expr= x+y, sense=maximize)

# opt = SolverFactory('glpk')
# opt = SolverFactory('gurobi')
# opt = SolverFactory('cbc', executable='C:\\cbc\\bin\\cbc.exe')
opt = SolverFactory('cplex', executable='C:\\CPLEX_Studio_Community201\\cplex\\bin\\x64_win64\\cplex.exe')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n------------------------')
print('x=',x_value)
print(f'y= {y_value}')
