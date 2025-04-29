import highspy

h = highspy.Highs()
status = h.readModel('escala_enfermeiros.mps')
print("Leitura MPS status:", status)

h.run()
sol = h.getSolution()
print("x =", [int(round(v)) for v in sol.col_value])