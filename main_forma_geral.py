import highspy
import numpy as np

# Inicializa o ambiente HiGHS
h = highspy.Highs()

# Adiciona variáveis (x1, x2, x3, x4, x5, x6)
# Bounds padrão: 0 <= xi <= infinito, exceto x6 >= 20
h.addVar(0, highspy.kHighsInf)  # x1 (índice 0)
h.addVar(0, highspy.kHighsInf)  # x2 (índice 1)
h.addVar(0, highspy.kHighsInf)  # x3 (índice 2)
h.addVar(0, highspy.kHighsInf)  # x4 (índice 3)
h.addVar(0, highspy.kHighsInf)  # x5 (índice 4)
h.addVar(20, highspy.kHighsInf) # x6 (índice 5) - mínimo 20

# Define os coeficientes da função objetivo
h.changeColCost(0, 1)    # x1 tem custo 1
h.changeColCost(1, 1)    # x2 tem custo 1
h.changeColCost(2, 1)    # x3 tem custo 1
h.changeColCost(3, 1.5)  # x4 tem custo 1.5
h.changeColCost(4, 2)    # x5 tem custo 2
h.changeColCost(5, 1)    # x6 tem custo 1

# Adiciona restrições (turnos)
inf = highspy.kHighsInf

# Restrição C1: x6 + x1 >= 50
indices = np.array([5, 0])  # x6 (índice 5) e x1 (índice 0)
values = np.array([1.0, 1.0])
h.addRow(50, inf, 2, indices, values)

# Restrição C2: x1 + x2 >= 60
indices = np.array([0, 1])
values = np.array([1.0, 1.0])
h.addRow(60, inf, 2, indices, values)

# Restrição C3: x2 + x3 >= 50
indices = np.array([1, 2])
values = np.array([1.0, 1.0])
h.addRow(50, inf, 2, indices, values)

# Restrição C4: x3 + x4 >= 40
indices = np.array([2, 3])
values = np.array([1.0, 1.0])
h.addRow(40, inf, 2, indices, values)

# Restrição C5: x4 + x5 >= 30
indices = np.array([3, 4])
values = np.array([1.0, 1.0])
h.addRow(30, inf, 2, indices, values)

# Restrição C6: x6 >= 20 (já garantido pelo bound, mas pode ser redundante)
indices = np.array([5])
values = np.array([1.0])
h.addRow(20, inf, 1, indices, values)


# Define variáveis como INTEIRAS
for i in range(6):  # Índices de 0 a 5 (x1 a x6)
    h.changeColIntegrality(i, highspy.HighsVarType.kInteger)

# Resolve o modelo
h.run()

# Exibe a solução
solution = h.getSolution()
print("Solução ótima:")
print(f"x1 = {solution.col_value}")
#print(f"x1 = {solution.col_value[0]}")
#print(f"x2 = {solution.col_value[1]}")
#print(f"x3 = {solution.col_value[2]}")
#print(f"x4 = {solution.col_value[3]}")
#print(f"x5 = {solution.col_value[4]}")
#print(f"x6 = {solution.col_value[5]}")
#print(f"Custo total: {h.getObjectiveValue()}")