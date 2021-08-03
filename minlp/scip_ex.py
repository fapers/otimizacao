from pyscipopt import Model

model = Model('exemplo')
# Variáveis de definição
x = model.addVar('x', vtype='INTEGER')
y = model.addVar('y', vtype='INTEGER')
z = model.addVar('z')
# Função Objetivo
model.setObjective(z, sense='maximize')
# Restrições
model.addCons(z==x+y*x)
model.addCons(-x+2*y*x<=8)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)
# Solução
model.optimize()
sol = model.getBestSol()
print('x=',sol[x])
print('y=',sol[y])