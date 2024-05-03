def trianguloAEstrella(impedancia):
    r1, r2, r3 = impedancia
    R1 = r2 * r3 / (r1 + r2 + r3)
    R2 = r1 * r3 / (r1 + r2 + r3)
    R3 = r1 * r2 / (r1 + r2 + r3)
    return [R1, R2, R3]
def estrellaATriangulo (impedancia):
    R1, R2, R3 = impedancia
    r1 = (R1*R2) + (R1*R3) + (R2*R3) / R1
    r2 = (R1*R2) + (R1*R3) + (R2*R3) / R2
    r3 = (R1*R2) + (R1*R3) + (R2*R3) / R3
    return [r1, r2, r3]
 # Resolverlo
triangulo = [100, 180, 220]
resistencia = trianguloAEstrella(triangulo)
print("El valor de las resistencias en estrella son: ", resistencia, " Ohmios")
