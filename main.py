import persistencia_json as pj
lista_coches = list()
while True:
    marca = input("Marca de coche:")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    linea = {}
    linea["Marca coche"] = marca
    linea["Modelo"] = modelo
    linea["Combustible"] = combustible
    linea["Cilindrada"] = cilindrada
    lista_coches.append(linea)
print("Lista coches:\n", lista_coches)
pj.store(lista_coches, )
         "coches.txt")