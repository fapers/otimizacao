import ortools.linear_solver.pywraplp as otlp

# solver = otlp.Solver('teste',otlp.Solver.GLOP_LINEAR_PROGRAMMING)
# solver = otlp.Solver('teste',otlp.Solver.GUROBI_LINEAR_PROGRAMMING)
# solver = otlp.Solver('teste',otlp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)
# solver = otlp.Solver('teste',otlp.Solver.GUROBI_MIXED_INTEGER_PROGRAMMING)
solver = otlp.Solver('teste',otlp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# Variáveis
x = solver.NumVar(0,10,'x')
y = solver.NumVar(0,10,'y')

# Restrições
solver.Add(-x+2*y<=8)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

# Função objetivo
solver.Maximize(x+y)

results = solver.Solve()

if results==otlp.Solver.OPTIMAL:
    print('Resultado Encontrado!')
else:
    print('Resultado NÃO encontrado')

print(f'x={x.solution_value()}')
print(f'y={y.solution_value()}')
