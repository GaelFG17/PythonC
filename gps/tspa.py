import math
from heapq import heappop, heappush
from coord import colindaciones, coord

# Función para calcular la distancia euclidiana entre dos ciudades
def distancia(ciudad1, ciudad2):
    lat1, lon1 = coord[ciudad1]
    lat2, lon2 = coord[ciudad2]
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)


def heuristica(ciudad_actual, destino):
    return distancia(ciudad_actual, destino)

def a_star(origen, destino):
    heap = [(0 + heuristica(origen, destino), 0, origen)]
    visitados = set()
    distancia_minima = {ciudad: float('inf') for ciudad in coord}
    distancia_minima[origen] = 0
    ruta = {origen: [origen]}