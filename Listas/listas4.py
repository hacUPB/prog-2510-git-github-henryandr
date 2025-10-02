# Lista de componentes con sus masas (kg) y posiciones (m)
componentes = ["motor izquierdo", "motor derecho", "fuselaje", "ala izquierda", "ala derecha", "cola"]
masas = [1200, 1200, 5000, 800, 800, 600]
posiciones_x = [-2, 2, 0, -2, 2, -6]

# Cálculo del centro de masa en eje X sin list comprehensions
masa_total = 0
momento_total = 0

# for i in range(len(masas)):
#     masa_total += masas[i]
#     momento_total += masas[i] * posiciones_x[i]
for m, p in zip(masas, posiciones_x):
    masa_total += m
    momento_total += m*p

centro_masa_x = momento_total / masa_total

print(f"Centro de masa en eje X: {centro_masa_x:.2f} m")

#Imprimir cuánta masa hay en cada componente del avión
for comp, masa in zip(componentes, masas):
    print(f"{comp:20} --> {masa:10} kg")