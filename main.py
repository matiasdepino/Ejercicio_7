lista_datos = []
while True:
    nombre = input("Ingrese el nombre deseado :")
    if nombre == "fin":
        break
    telefono = input("Ingrese el número de teléfono :")
    linea = {}
    linea["Nombre"] = nombre
    linea["Número de Teléfono"] = telefono
    lista_datos.append(linea)
for linea in lista_datos:
        print("Datos:", linea)
