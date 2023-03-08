import csv


# Funcion que muestra las opciones del programa
# def mostrarOpciones():
#     print(" **** Menu del programa **** ", end="\n\n")
#     print("1. Agregar un nuevo registro")
#     print("2. Buscar un registro por su clave y mostrar sus valores")
#     print("3. Borrar un registro a partir de su clave")
#     print("4. Listar todos los registros en formato de tabla")
#     print("5. Salir")

# Menu que muestra las opciones y evalua la opcion seleccionada

# while True:
#     print(mostrarOpciones())
#     opt = input("Seleccione una opcion (1-5): ")
#     print("\n")
#     if opt=="1":
#         print("Agregar un nuevo registro", end="\n\n")
#     elif opt=="2":
#         print("Buscar un registro por su clave y mostrar sus valores", end="\n\n")
#     elif opt=="3":
#         print("Borrar un registro a partir de su clave", end="\n\n")
#     elif opt=="4":
#         print("Listar todos los registros en formato de tabla", end="\n\n")
#     elif opt=="5":
#         print("Adios", end="\n\n")
#         break
#     else:
#         print("Opcion  invalida", end="\n\n")


# with open(r"C:\Users\joni-\Documents\FSI_EPDs\Grupo_8\P1\8_ApartmentsLite.csv", "r") as archivo:
#     contenido = archivo.read()
#   # for row in contenido:
#     print(contenido)



with open('8_ApartmentsLite.csv', 'r', encoding='utf-8') as archivo:
    contenido = csv.reader(archivo,delimiter=',')
    # print(contenido)
    next(contenido)

    diccionario1 = dict()
    lista_nums_registros = list()
    for linea in contenido:
        tupla_valor = tuple(linea)
        lista_nums_registros.append(tupla_valor[0])
        diccionario1[(tupla_valor[0], tupla_valor[-1])] = tupla_valor


print(lista_nums_registros)
print(diccionario1)

# Recorrido para obtener las tuplas clave.
lista_claves = list()
for clave in diccionario1.keys():
    lista_claves.append(clave)
print(lista_claves)
# Recorrido para obtener el valor del primer indice de las tuplas clave.
lista_valores = []
for tupla in lista_claves:
    lista_valores.append(tupla[0])
print(lista_valores)




def nuevo_registro():
#   Nuevo registro generado a partir de una lista modelo. Lista que hace referencia a los indices de la cabecera del dataset.
    lista_modelo = ["numero", "sumary", "description", "location", "photo", "recomendado", "price", "size", "rooms",
                    "price/m2", "bathrooms", "Num Photos", "type", "region"]
    print("Introdusca nuevo registro")

#   "lista_nueva" que contendra el mismo numero de elementos que la "lista_modelo"
    lista_nueva = []
    i = 0
    tam_lista_modelo = len(lista_modelo)
    tam_lista_nueva = len(lista_nueva)
#   Bucle que evalua el tamano de la lista nueva.
    while tam_lista_nueva < tam_lista_modelo:
        elemento_lista_nueva = str(input("Introdusca " + lista_modelo[i] + ": "))
        lista_nueva.append(elemento_lista_nueva)
        tam_lista_nueva = len(lista_nueva)
        i = i + 1
#   La nueva lista generada pasa a tomar el mismo formato que diccionario1.
    tupla_list_nueva = tuple(lista_nueva)
    # print(tupla_list_nueva)

    diccionario2 = dict()
    diccionario2[(tupla_list_nueva[0], tupla_list_nueva[-1])] = tupla_list_nueva


#   Evaluar si el primer indice de la nueva lista y el primer indice de la tupla clave son iguales
    print(tupla_list_nueva[0])
    valor = lista_valores.index(tupla_list_nueva[0])
    print(valor)
    print(lista_valores[valor])
#     print("Registro no valido. El nuevo registro ya existen")

nuevo_registro()

# def valor_valido():
#     valor = lista_valores.index(tupla_list_nueva[0])


