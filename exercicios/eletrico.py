from pandas.core.algorithms import SelectN
import pyomo.environ as pyo, numpy as np, pandas as pd
from pyomo.environ import *
from pyomo.opt import SolverFactory

# entradas
barras = pd.read_excel('sist_eletrico.xlsx', sheet_name='barras')
geracao = pd.read_excel('sist_eletrico.xlsx', sheet_name='geracao')
carga = pd.read_excel('sist_eletrico.xlsx', sheet_name='carga')
linha = pd.read_excel('sist_eletrico.xlsx', sheet_name='linha')
Nb = len(barras)
Ng = len(geracao)
Nd = len(carga)
Nl = len(linha)

# modelo
model = pyo.ConcreteModel()
model.Pg = pyo.Var(range(Ng))
model.Pl = pyo.Var(range(Nl))
model.teta = pyo.Var(range(Nb), bounds=(-np.pi, np.pi))
Pg = model.Pg
Pl = model.Pl
teta = model.teta

# objetivo
model.obj = pyo.Objective(expr=sum([Pg[g]*geracao.custo[g] for g in geracao.index]), sense=minimize)

# balanço de potência
model.balanco = pyo.ConstraintList()
for n in barras.index:
    sum_Pg = sum([Pg[g] for g in geracao.index[geracao.barra==n]])
    sum_Pls = sum([Pl[l] for l in linha.index[linha.barra_de==n]])
    sum_Plr = sum([Pl[l] for l in linha.index[linha.barra_para==n]])
    sum_Pd = sum([carga.carga[d] for d in carga.index[carga.barra==n]])
    model.balanco.add(expr=sum_Pg - sum_Pls + sum_Plr == sum_Pd)
    
# fluxo de potência
model.fluxo = pyo.ConstraintList()
