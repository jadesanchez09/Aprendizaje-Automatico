import numpy as np
import matplotlib.pyplot as plt

# Datos que queremos agrupar
datos = np.array([
    [1, 2],
    [2, 1],
    [2, 3],
    [8, 8],
    [9, 8],
    [8, 9]
])

# Número de grupos
k = 2

# Elegimos centroides iniciales
centroides = np.array([
    [1, 2],
    [8, 8]
])

# Repetimos varias veces el proceso 
for iteracion in range(10):

    grupos = []

    # Revisamos cada dato
    for punto in datos:

        distancias = []

        # Calculamos su distancia a cada centroide
        for centroide in centroides:
            distancia = np.sqrt(
                (punto[0] - centroide[0]) ** 2 +
                (punto[1] - centroide[1]) ** 2
            )

            distancias.append(distancia)

        # Guardamos el grupo del centroide más cercano
        grupo = np.argmin(distancias)
        grupos.append(grupo)

    grupos = np.array(grupos)

    # Calculamos los nuevos centroides
    nuevos_centroides = []

    for i in range(k):
        puntos_grupo = datos[grupos == i]

        nuevo_centroide = np.mean(puntos_grupo, axis=0)

        nuevos_centroides.append(nuevo_centroide)

    nuevos_centroides = np.array(nuevos_centroides)

    # Actualizamos los centroides
    centroides = nuevos_centroides


print("Grupos:")
print(grupos)

print("\nCentroides finales:")
print(centroides)


# Mostrar los puntos
plt.scatter(datos[:, 0], datos[:, 1], c=grupos)

# Mostrar los centroides
plt.scatter(
    centroides[:, 0],
    centroides[:, 1],
    marker="X",
    s=200
)

plt.title("K-Means")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()