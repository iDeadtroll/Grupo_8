import csv
with open('8_ApartmentsLite.csv', 'r', encoding='utf-8') as archivo:
    contenido = csv.reader(archivo,delimiter=',')
    # print(contenido)
    next(contenido)

    diccionario1 = dict()
    lista_nums_registros = list()
    for linea in contenido:
        tupla_valor = tuple(linea)
        lista_nums_registros.append(tupla_valor[0])
        tupla_clave = (tupla_valor[0], tupla_valor[-1])
        diccionario1[tupla_clave] = tupla_valor

# print(lista_nums_registros)
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
# print(lista_valores)

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
        elemento_lista_nueva = str(input("Introduzca " + lista_modelo[i] + ": "))
        lista_nueva.append(elemento_lista_nueva)
        tam_lista_nueva = len(lista_nueva)
        i = i + 1
#   La nueva lista generada pasa a tomar el mismo formato que diccionario1.
    tupla_list_nueva = tuple(lista_nueva)
    # print(tupla_list_nueva)

    diccionario2 = dict()
    diccionario2[(tupla_list_nueva[0], tupla_list_nueva[-1])] = tupla_list_nueva


#   Evaluar si el primer indice de la nueva lista y el primer indice de la tupla clave son iguales

    # print(tupla_list_nueva[0])
    # valor = lista_valores.index(tupla_list_nueva[0])
    # print(valor)
    # print(lista_valores[valor])

#     print("Registro no valido. El nuevo registro ya existen")


# Funcion que muestra las opciones del programa
def tabla_diccionario():
    for tupla_clave, tupla_valor in diccionario1.items():
        print(f'{tupla_valor}')
def borrar_registro():
    print(diccionario1)
    print("Clave formada por una tupla (prime indice, segundo indice)")
    a = input("Introduce el primer indice de la tupla")
    b = input("Introduce el segundo indice de la tupla")
    t = (a, b)
    diccionario1.pop(t)
    print(diccionario1)



def busca_valor_clave():
    print("Clave formada por una tupla (prime indice, segundo indice)")
    a = input("Introduce el primer indice de la tupla")
    b = input("Introduce el segundo indice de la tupla")
    t = (a, b)
    valor = diccionario1.get(t)
    print(valor)

def mostrarOpciones():
    print(" **** Menu del programa **** ", end="\n\n")
    print("1. Agregar un nuevo registro")
    print("2. Buscar un registro por su clave y mostrar sus valores")
    print("3. Borrar un registro a partir de su clave")
    print("4. Listar todos los registros en formato de tabla")
    print("5. Salir")

# Menu que muestra las opciones y evalua la opcion seleccionada


# while True:
#     print(mostrarOpciones())
#     opt = input("Seleccione una opcion (1-5): ")
#     print("\n")
#     if opt=="1":
#         print("Opcion: Agregar nuevo registro", end="\n\n")
#         nuevo_registro()
#     elif opt=="2":
#         print("Opcion: Buscar un registro por su clave y mostrar sus valores", end="\n\n")
#         # busca_valor_clave()
#     elif opt=="3":
#         print("Borrar un registro a partir de su clave", end="\n\n")
#     elif opt=="4":
#         print("Listar todos los registros en formato de tabla", end="\n\n")
#     elif opt=="5":
#         print("Adios", end="\n\n")
#         break
#     else:
#         print("Opcion  invalida", end="\n\n")

print(mostrarOpciones())
opt = input("Seleccione una opcion (1-5): ")
print("\n")

match opt:
    case "1":
        print("Opcion: Agregar nuevo registro", end="\n\n")
        nuevo_registro()
    case "2":
        print("Opcion: Buscar un registro por su clave y mostrar sus valores", end="\n\n")
        busca_valor_clave()
    case "3":
        print("Borrar un registro a partir de su clave", end="\n\n")
        borrar_registro()
    case "4":
        print("Listar todos los registros en formato de tabla", end="\n\n")
        tabla_diccionario()

    # case "5":



# with open(r"C:\Users\joni-\Documents\FSI_EPDs\Grupo_8\P1\8_ApartmentsLite.csv", "r") as archivo:
#     contenido = archivo.read()
#   # for row in contenido:
#     print(contenido)
