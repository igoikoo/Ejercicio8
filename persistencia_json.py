def store(var,filename):
    pj.dump(pj.dumps(lista_coches), open("lista_coches.data", "w"))

def retrieve(main):
    return pj.loads(pj.load(open(filename, "r")))
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