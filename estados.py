import estados as nx

grafo = nx.Graph()

estados = ["Oaxaca", "Chiapas", "Yucatán", "Guadalajara", "Michoacán", "Monterrey", "Guanajuato"]
for estado in estados:
    grafo.add_node(estado)

relaciones = [("Oaxaca", "Chiapas", 300),
              ("Oaxaca", "Yucatán", 500),
              ("Oaxaca", "Guadalajara", 250),
              ("Oaxaca", "Michoacán", 150),
              ("Oaxaca", "Monterrey", 50),
              ("Oaxaca", "Guanajuato", 550),
              ("Chiapas", "Yucatán", 500),
              ("Chiapas", "Guadalajara", 250),
              ("Chiapas", "Michoacán", 150),
              ("Chiapas", "Monterrey", 50),
              ("Chiapas", "Guanajuato", 550),
              ("Yucatán", "Guadalajara", 250),
              ("Yucatán", "Michoacán", 150),
              ("Yucatán", "Monterrey", 50),
              ("Yucatán", "Guanajuato", 550),
              ("Guadalajara", "Michoacán", 150),
              ("Guadalajara", "Monterrey", 50),
              ("Guadalajara", "Guanajuato", 550),
              ("Michoacán", "Monterrey", 50),
              ("Michoacán", "Guanajuato", 550),
              ("Monterrey", "Guanajuato", 550)]

for origen, destino, costo in relaciones:
    grafo.add_edge(origen, destino, weight=costo)

def calcular_costo(grafo, origen, destino):
    return nx.shortest_path_length(grafo, origen, destino, weight='weight')

def menu():
    print("Seleccione un estado para ver su costo de traslado:")
    for i, estado in enumerate(estados):
        print(f"{i + 1}. {estado}")
    opcion = int(input("Opción: "))
    return opcion

opcion = menu()
while opcion < 1 or opcion > len(estados):
    print("Opción inválida. Inténtelo de nuevo.")
    opcion = menu()

origen = estados[opcion - 1]

print(f"\nCosto de traslado desde {origen}:")
for destino in estados:
    if destino != origen:
        costo = calcular_costo(grafo, origen, destino)
        print(f"{destino}: ${costo}")
