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

    while True:
        try:

            nombre = input(
                "Ingrese el nombre del País que desea agregar: ").strip().lower()
            # Verifico que el nombre no esté vacío
            if nombre == "":
                raise ValueError("Nombre vacío.")

            # Verifico que el país que se desea ingresar no exista para evitar duplicados.
            encontrado = False
            for pais in lista_paises:

                if pais["nombre"].lower() == nombre:
                    encontrado = True
                    break
            if encontrado:
                raise ValueError("El país que desea ingresar ya existe.")

            break
        # De haber un error lo capturo y muestro por pantalla.
        except ValueError as error:
            print("Ha ocurrido el siguiente error: ", error)

    while True:
        try:

            poblacion = int(input("Ingrese el número de la población: "))
            # Verifico que el número proporcionado no sea negativo ni 0.
            if poblacion <= 0:
                raise ValueError(
                    "La población nunca puede ser menor o igual a 0.")

            break

        except ValueError as error:
            print("Ha ocurrido el siguiente error: ", error)

    while True:
        try:

            superficie = int(
                input("Ingrese el número de la superficie en km²: "))

            if superficie <= 0:
                raise ValueError(
                    "La superficie nunca puede ser menor o igual a 0.")

            break

        except ValueError as error:
            print("Ha ocurrido el siguiente error: ", error)

    while True:
        try:

            continente = input(
                "Ingrese el nombre del continente al que pertenece su país: ").strip().lower()

            if continente == "":
                raise ValueError("Nombre del continente vacío.")

            break
        except ValueError as error:
            print("Ha ocurrido el siguiente error: ", error)

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    try:
        with open(ARCHIVO, "a", encoding="utf-8", newline="") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=[
                "nombre", "poblacion", "superficie", "continente"])
            writer.writerow(nuevo_pais)

        lista_paises.append(nuevo_pais)
        print(f"{nombre.title()} agregado correctamente.")

    # Valido que el archivo no tenga problemas de permisos o este bloqueado
    except PermissionError:
        print("Error: no se tienen permisos para escribir en el archivo.")
    # Valido que no haya errores como una ruta mal definida.
    except OSError as error:
        print("Error al intentar escribir en el archivo: ", error)


def actualizar_pais(lista_paises):
    """Busca un país por nombre y actualiza su población y/o superficie."""

    while True:
        try:

            print("Actualizar datos de un país")

            busqueda = input(
                "\nIngrese el nombre del país que desea actualizar: ").strip().lower()

            if busqueda == "":
                raise ValueError("Nombre vacío.")

            encontrado = False

            for pais in lista_paises:

                if pais["nombre"].lower() == busqueda:

                    encontrado = True
                    break

            if not encontrado:
                raise ValueError("El país buscado no forma parte del dataset.")

            break

        except ValueError as error:
            print("\nHa ocurrido el siguiente error: ", error)

    while True:

        try:
            print("\n¿Qúe desea actualizar?")
            print("1. Población")
            print("2. Superficie")

            opcion = int(input("\nSeleccione una opción [1-2]: "))

            if not opcion in [1, 2]:
                raise ValueError("Opción fuera de rango.")

            else:
                break

        except ValueError as error:
            print("\nHa ocurrido el siguiente error: ", error)

    if opcion == 1:

        while True:
            try:

                nueva_poblacion = int(
                    input(f"\nIngrese la nueva población de {busqueda}: "))

                if nueva_poblacion <= 0:
                    raise ValueError(
                        "La población no puede ser menor o igual a 0.")

                break

            except ValueError as error:
                print("Ha ocurrido el siguiente error: ", error)

        for pais in lista_paises:

            if pais["nombre"].lower() == busqueda:

                pais["poblacion"] = nueva_poblacion

                print("\nPoblación modificada con éxito.")
                print("Volviendo al menú principal...")

    elif opcion == 2:

        while True:
            try:

                nueva_superficie = int(
                    input(f"\nIngrese la nueva superficie de {busqueda}: "))

                if nueva_superficie <= 0:
                    raise ValueError(
                        "La superficie no puede ser menor o igual a 0.")

                break

            except ValueError as error:
                print("\nHa ocurrido el siguiente error: ", error)

        for pais in lista_paises:

            if pais["nombre"].lower() == busqueda:

                pais["superficie"] = nueva_superficie

                print("Superficie modificada con éxito.")
                print("Volviendo al menú principal...")

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:

        escritor = csv.DictWriter(archivo, fieldnames=[
            "nombre", "poblacion", "superficie", "continente"])

        escritor.writeheader()
        escritor.writerows(lista_paises)


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


ARCHIVO = "paises.csv"
lista_paises = cargar_csv(ARCHIVO)


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
