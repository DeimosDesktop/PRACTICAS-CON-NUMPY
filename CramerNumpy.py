import numpy as np
#________________________#
#ecuaciones = i1, i2 
#_________________________#
ecuacion1 = [220,-120,24]
ecuacion2 = [-120,300,-20]
det1 = np.array([[ecuacion1[1], ecuacion1[2]], [ecuacion2[1], ecuacion2[2]]])
det2 = np.array([[ecuacion1[0], ecuacion1[2]], [ecuacion2[0], ecuacion2[2]]])
detComun = np.array([[ecuacion1[0], ecuacion1[1]], [ecuacion2[0], ecuacion2[1]]])

# Calcular el determinante
solI1 = np.linalg.det(det1) / np.linalg.det(detComun)
solI2 = np.linalg.det(det2) / np.linalg.det(detComun)

print("La intensidad I1 es de {} Amperios". format(solI1))
print("La intensidad I2 es de {} Amperios". format(solI2))
