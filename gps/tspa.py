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
    
    while heap:
        _, costo_acumulado, ciudad_actual = heappop(heap)
        if ciudad_actual in visitados:
            continue

        visitados.add(ciudad_actual)

        if ciudad_actual == destino:
            break
        
        for ciudad_vecina, distancia_vecina in colindaciones[ciudad_actual].items():
            if ciudad_vecina not in visitados:
                distancia_nueva = costo_acumulado + distancia_vecina

                if distancia_nueva < distancia_minima[ciudad_vecina]:
                    distancia_minima[ciudad_vecina] = distancia_nueva
                    heappush(heap, (distancia_nueva + heuristica(ciudad_vecina, destino), distancia_nueva, ciudad_vecina))
                    ruta[ciudad_vecina] = ruta[ciudad_actual] + [ciudad_vecina]
                    
    return ruta[destino], distancia_minima[destino]

def obtenerruta(origen, destino):
    ruta, distancia = a_star(origen, destino)
    print(ruta)
    print(distancia)
    return ruta, distancia