import highspy

h = highspy.Highs()
h.readModel('escala_enfermeiros.mps')   # agora sem erro de parser
h.run()
print("Status:", h.getModelStatus())
sol = h.getSolution()
print("x =", [int(v) for v in sol.col_value])
