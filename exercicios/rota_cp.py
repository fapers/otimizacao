# Author: Fábio
# APP: Rotas com GA
# Data: 03/08/2021

# MODELAGEM
# Variáveis: binária x_ij
# Estamos definindo se um caminho foi escolhido ou não 1 para sim e 0 para não
# 
# Função Objetivo: Minimizar a soma de todos (x_ij * Dx_ij)
# Estamos minimizando a soma das distância dos caminhos escolhidos
# 
# Restrições: 
# C1) Nó de origem: define que um dos caminhos escolhidos precisa ser igual a 1,
# logo a somatória de todos os caminhos de saída precisa ser igual a 1.
# 
# C2) Nó de destino: um dos caminhos de entrada precisa ser igual a 1,
# logo a somatória de todos os caminhos de entrada precisa ser igual a 1.
#
# Para os demais nós que não são origem nem destino precisamos que a soma
# de todos os caminhos que entram sejam igual a 1 ou 0, logo a somatória 
# será menor ou igual a 1. O mesmo se aplica aos caminhos que saem.
# C3) Nó de saída: somatória menor ou igual a 1
# 
# C4) Nó de entrada: somatória menor ou igual a 1
# 
# C5) Caminho: se algum caminho de entrada num determinado nó foi escolhido,
# então um caminho de saída deverá também ser escolhido.

# Como se trata de um problema combinatorial
# Criamos uma planilha do excel com as abas nos e caminhos
# rotas_inputs.xlsx
# nos
# no	desc
# 1	    origem
# 2	    meio
# 3	    meio
# 4	    meio
# 5	    meio
# 6	    meio
# 7	    destino
# 
# caminhos
# no_de	no_para	distancia
# 1	    2	    220
# 1	    3	    1500
# 2	    4	    650
# 2	    5	    900
# 4	    7	    500
# 5	    7	    400
# 3	    6	    500
# 6	    7	    400

# como estamos trabalhando com excel utilizamos o pandas
import pandas as pd, numpy as np
# vamos utilizar o Constraint Problem
from ortools.sat.python import cp_model

# -> entrada
nos = pd.read_excel('exercicios/rotas_inputs.xlsx', sheet_name='nos')
caminhos = pd.read_excel('exercicios/rotas_inputs.xlsx', sheet_name='caminhos')
n_nos = len(nos)
n_caminhos = len(caminhos)

# -> modelo
model = cp_model.CpModel()
x = np.zeros(n_caminhos).tolist()
for c in caminhos.index:
    # Caso duas dimensões f'x[{[x, y]}]
    x[c] = model.NewIntVar(0,1, f'x[{[c]}]')
    
# -> Função objetivo
model.Minimize(sum([x[c] * caminhos.distancia[c] for c in caminhos.index]))

# -> Restrições
# Define os nos de origem e destino
no_origem = int(nos.no[nos.desc=='origem'])
no_destino = int(nos.no[nos.desc=='destino'])

# Define os outros nos
model.Add(sum([x[c] for c in caminhos.index[caminhos.no_de==no_origem]])==1)
model.Add(sum([x[c] for c in caminhos.index[caminhos.no_para==no_destino]])==1)

# Somatório
for no in nos.no[nos.desc=='meio']:
    sum_entra = sum([x[c] for c in caminhos.index[caminhos.no_para==no]])
    sum_sai = sum([x[c] for c in caminhos.index[caminhos.no_de==no]])
    model.Add(sum_sai <= 1)
    model.Add(sum_entra <= 1)
    model.Add(sum_entra == sum_sai)
    
# -> Solução
solver = cp_model.CpSolver()
status = solver.Solve(model)

# -> Impressão
print(f'Status = {solver.StatusName(status)}')
print(f'FO = {solver.ObjectiveValue()}')
caminhos['ativado'] = 0
for c in caminhos.index:
    caminhos.ativado[c] = solver.Value(x[c])
print(caminhos)

print('Rota escolhida')
for c in caminhos.index[caminhos.ativado==1]:
    print(f'X{caminhos.no_de[c]}{caminhos.no_para[c]} - {caminhos.distancia[c]}')
