import pandas as pd, numpy as np
from geneticalgorithm import geneticalgorithm as ga

# Entrada
nos = pd.read_excel('exercicios/rotas_inputs.xlsx', sheet_name='nos')
caminhos = pd.read_excel('exercicios/rotas_inputs.xlsx', sheet_name='caminhos')
n_nos = len(nos)
n_caminhos = len(caminhos)
