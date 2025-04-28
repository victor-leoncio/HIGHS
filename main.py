import highspy
import numpy as np

h = highspy.Highs()
inf = highspy.kHighsInf

#x0 = h.addVariable(lb = 0, ub = inf)
x1 = h.addVariable(lb = 0, ub = inf)
x2 = h.addVariable(lb = 0, ub = inf)
x3 = h.addVariable(lb = 0, ub = inf)
x4 = h.addVariable(lb = 0, ub = inf)
x5 = h.addVariable(lb = 0, ub = inf)
x6 = h.addVariable(lb = 0, ub = inf)

h.addConstr(x6 + x1 >= 50)
h.addConstr(x1 + x2 >= 60)
h.addConstr(x2 + x3 >= 50)
h.addConstr(x3 + x4 >= 40)
h.addConstr(x4 + x5 >= 30)
h.addConstr(x5 + x6 >= 20)

h.minimize(x1 + x2 + x3 + (1.5*x4) + (2*x5) + x6)

h.run()

solution = h.getSolution()
basis = h.getBasis()
info = h.getInfo()
model_status = h.getModelStatus()
model_solution = h.getSolution()

print()
print(f"Colunas = {model_solution.col_value}")
print(f"Colunas dual = {model_solution.col_dual}")
print(f"Linhas = {model_solution.row_value}")
print(f"Linhas dual = {model_solution.row_dual}")
print(f"Valido = {model_solution.value_valid}")
print(f"Dual Valido = {model_solution.dual_valid}")


#print('Model status = ', h.modelStatusToString(model_status))
#print()
#print('Optimal objective = ', info.objective_function_value)
#print('Iteration count = ', info.simplex_iteration_count)
#print('Primal solution status = ', h.solutionStatusToString(info.primal_solution_status))
#print('Dual solution status = ', h.solutionStatusToString(info.dual_solution_status))
#print('Basis validity = ', h.basisValidityToString(info.basis_validity))
