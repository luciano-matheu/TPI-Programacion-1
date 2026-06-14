import csv


def cargar_csv(nombre_archivo):

    lista_paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for pais in lector:

                try:
                    lista_paises.append({
                        "nombre": pais["nombre"].strip(),
                        "poblacion": int(pais["poblacion"]),
                        "superficie": int(pais["superficie"]),
                        "continente": pais["continente"].strip()
                    })

                except ValueError as error:
                    print("Ha ocurrido un error de conversión: ", error)

                except KeyError as error:
                    print(f"Falta la columna: {error}")

    except FileNotFoundError:
        print("El archivo no existe en la ubicación brindada.")

    return lista_paises


def mostrar_pais(pais):
    """Muestra los datos de un país formateados."""
    print(f"  País       : {pais['nombre'].title()}")
    print(f"  Población  : {pais['poblacion']:,}")
    print(f"  Superficie : {pais['superficie']:,} km²")
    print(f"  Continente : {pais['continente'].title()}")
    print("-"*30)


def listar_paises(lista_paises):
    """Muestra todos los países cargados en el sistema."""
    if not lista_paises:
        print("No hay países cargados.")
        return

    print(f"\n===== PAÍSES CARGADOS ({len(lista_paises)}) =====")
    for pais in lista_paises:
        mostrar_pais(pais)


def agregar_pais(lista_paises):
    """Solicita datos al usuario y agrega un nuevo país a la lista."""
    pass


def actualizar_pais(lista_paises):
    """Busca un país por nombre y actualiza su población y/o superficie."""
    pass


def buscar_por_nombre(lista_paises):
    """Busca y muestra países cuyo nombre coincida parcial o exactamente."""
    pass


def filtrar_paises(lista_paises):
    """Muestra un submenú para filtrar por continente, población o superficie."""
    pass


def ordenar_paises(lista_paises):
    """Muestra un submenú para ordenar por nombre, población o superficie."""
    pass


def mostrar_estadisticas(lista_paises):
    """Muestra estadísticas generales del dataset."""
    pass


lista_paises = cargar_csv("paises.csv")


# Main
while True:
    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1. Ver todos los países cargados")
    print("2. Agregar país")
    print("3. Actualizar país")
    print("4. Buscar por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Salir")

    try:
        opcion = int(input("\nElegí una opción: "))

        if opcion == 1:
            listar_paises(lista_paises)

        elif opcion == 2:
            agregar_pais(lista_paises)

        elif opcion == 3:
            actualizar_pais(lista_paises)

        elif opcion == 4:
            buscar_por_nombre(lista_paises)

        elif opcion == 5:
            filtrar_paises(lista_paises)

        elif opcion == 6:
            ordenar_paises(lista_paises)

        elif opcion == 7:
            mostrar_estadisticas(lista_paises)

        elif opcion == 8:
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Ingresá un número del 1 al 8.")

    except ValueError:
        print("Ingresá un número, no texto.")
