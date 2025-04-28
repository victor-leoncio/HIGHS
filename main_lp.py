import highspy
h = highspy.Highs()
h.readModel('escala_enfermeiros.lp')
h.run()
sol = h.getSolution()
print(sol.col_value)
