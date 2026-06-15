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

    try:
        # Actualizo el archivo CSV con los nuevos datos.
        with open(ARCHIVO, "w", encoding="utf-8") as archivo:

            escritor = csv.DictWriter(
                archivo,
                fieldnames=[
                    "nombre",
                    "poblacion",
                    "superficie",
                    "continente"
                ]
            )

            escritor.writeheader()
            escritor.writerows(lista_paises)

    except PermissionError:
        print("Error: no se tienen permisos para modificar el archivo.")

    except OSError as error:
        print("Error al intentar actualizar el archivo:", error)


def buscar_por_nombre(lista_paises):
    """Busca y muestra países cuyo nombre coincida parcial o exactamente."""

    while True:
        try:

            busqueda = input(
                "\nIngrese el nombre o parte del nombre del país que desea buscar: "
            ).strip().lower()

            if busqueda == "":
                raise ValueError("La búsqueda no puede estar vacía.")

            break

        except ValueError as error:
            print("\nHa ocurrido el siguiente error:", error)

    encontrados = False

    for pais in lista_paises:

        if busqueda in pais["nombre"].lower():

            print("-"*30)
            mostrar_pais(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron coincidencias.")


def filtrar_paises(lista_paises):
    """Muestra un submenú para filtrar por continente, población o superficie."""

    while True:
        try:
            print("\n¿Por qué desea filtrar?")
            print("1. Continente")
            print("2. Rango de población")
            print("3. Rango de superficie")

            opcion = int(input("Seleccione una opción [1-3]: "))

            if opcion not in [1, 2, 3]:
                raise ValueError("Opción fuera de rango.")

            break

        except ValueError as error:
            print("\nHa ocurrido el siguiente error:", error)

    if opcion == 1:

        while True:
            try:

                print("Busqueda por continente.")

                continente = input(
                    "\nIngrese el nombre del continente: "
                ).strip().lower()

                if continente == "":
                    raise ValueError("La búsqueda no puede estar vacía.")

                break

            except ValueError as error:
                print("\nHa ocurrido el siguiente error:", error)

        encontrados = False

        for pais in lista_paises:

            if pais["continente"].lower() == continente:

                print("-"*30)
                mostrar_pais(pais)
                encontrados = True

        if not encontrados:
            print("No se encontraron coincidencias.")

    elif opcion == 2:

        while True:

            try:
                print("Busqueda por rangos de Población.")

                rango_minimo = int(
                    input("Ingrese el rango mínimo de población: "))
                rango_maximo = int(
                    input("Ingrese el rango máximo de población: "))

                if rango_minimo < 0 or rango_maximo < 0:
                    raise ValueError("El rango no puede ser negativo")
                # Valido que el rango mínimo no sea más grande que el máximo
                if rango_minimo > rango_maximo:
                    raise ValueError(
                        "El rango mínimo no puede ser mayor al máximo.")

                break

            except ValueError as error:
                print("\nHa ocurrido el siguiente error:", error)

        encontrados = False

        for pais in lista_paises:

            if rango_minimo <= pais["poblacion"] <= rango_maximo:

                print("-"*30)
                mostrar_pais(pais)
                encontrados = True

        if not encontrados:
            print("No se encontraron coincidencias.")

    elif opcion == 3:

        while True:

            try:
                print("Busqueda por rangos de Superficie.")

                rango_minimo = int(
                    input("Ingrese el rango mínimo de superficie: "))
                rango_maximo = int(
                    input("Ingrese el rango máximo de superficie: "))

                if rango_minimo < 0 or rango_maximo < 0:
                    raise ValueError("El rango no puede ser negativo")

                if rango_minimo > rango_maximo:
                    raise ValueError(
                        "El rango mínimo no puede ser mayor al máximo.")

                break

            except ValueError as error:
                print("\nHa ocurrido el siguiente error:", error)

        encontrados = False

        for pais in lista_paises:

            if rango_minimo <= pais["superficie"] <= rango_maximo:

                print("-"*30)
                mostrar_pais(pais)
                encontrados = True

        if not encontrados:
            print("No se encontraron coincidencias.")


def ordenar_paises(lista_paises):
    """Muestra un submenú para ordenar por nombre, población o superficie."""

    while True:
        try:
            print("\n¿Por qué parámetro desea ordenar?")
            print("1. Nombre")
            print("2. Población")
            print("3. Superficie")

            opcion = int(input("Seleccione una opción [1-3]: "))

            if opcion not in [1, 2, 3]:
                raise ValueError("Opción fuera de rango.")

            break

        except ValueError as error:
            print("\nHa ocurrido el siguiente error:", error)

    while True:
        try:
            print("\n¿En qué orden desea mostrar los resultados?")
            print("1. Ascendente")
            print("2. Descendente")

            orden = int(input("Seleccione una opción [1-2]: "))

            if orden not in [1, 2]:
                raise ValueError("Opción fuera de rango.")

            break

        except ValueError as error:
            print("\nHa ocurrido el siguiente error:", error)

    # En esta variable obtengo si el usuario desea orden ascendente o descendente sabiendo True o False
    reverse = orden == 2

    if opcion == 1:
        # Filtro con sorted y uso lambda para indicar la clave por la que se tiene que guiar.
        lista_ordenada = sorted(
            lista_paises, key=lambda pais: pais["nombre"], reverse=reverse)

    elif opcion == 2:
        lista_ordenada = sorted(
            lista_paises, key=lambda pais: pais["poblacion"], reverse=reverse)

    elif opcion == 3:
        lista_ordenada = sorted(
            lista_paises, key=lambda pais: pais["superficie"], reverse=reverse)

    for pais in lista_ordenada:
        mostrar_pais(pais)


def mostrar_estadisticas(lista_paises):
    """Muestra estadísticas generales del dataset."""

    if not lista_paises:
        print("\nNo hay países cargados.")
        return

    # Hago uso de max y min para obtener el país con mayor y menor población.
    pais_mayor = max(lista_paises, key=lambda pais: pais["poblacion"])
    pais_menor = min(lista_paises, key=lambda pais: pais["poblacion"])

    # Lo mismo para la superficie.
    pais_mayor_superficie = max(
        lista_paises, key=lambda pais: pais["superficie"])

    pais_menor_superficie = min(
        lista_paises, key=lambda pais: pais["superficie"])

    # Inicializo 2 variables en 0 para luego calcular promedios.
    suma_poblacion = 0
    suma_superficie = 0

    # Hago uso de un diccionario para guardar continentes y cuantos países forman parte de él.
    continentes = {}

    for pais in lista_paises:

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1

        else:
            continentes[continente] = 1

    promedio_poblacion = suma_poblacion / len(lista_paises)
    promedio_superficie = suma_superficie / len(lista_paises)

    print("\nESTADÍSTICAS:")

    print(
        f"\nPaís con mayor población: "
        f"{pais_mayor['nombre'].title()} ({pais_mayor['poblacion']:,})"
    )

    print(
        f"País con menor población: "
        f"{pais_menor['nombre'].title()} ({pais_menor['poblacion']:,})"
    )

    print(
        f"\nPaís con mayor superficie: "
        f"{pais_mayor_superficie['nombre'].title()} "
        f"({pais_mayor_superficie['superficie']:,} km²)"
    )

    print(
        f"País con menor superficie: "
        f"{pais_menor_superficie['nombre'].title()} "
        f"({pais_menor_superficie['superficie']:,} km²)"
    )

    print(f"\nPromedio de población: {promedio_poblacion:,.2f}")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km²")

    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(f"- {continente.title()}: {cantidad}")


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
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Ingresá un número del 1 al 8.")

    except ValueError:
        print("Ingresá un número, no texto.")
