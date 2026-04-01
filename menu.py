# =================================================================================================================
# MÓDULO: menu.py | INTERFAZ DEL USUARIO Y CONTROL DEL FLUJO DEL PROGRAMA
# ESTE ARCHIVO SE ENCARGA DE MOSTRAR EL MENÚ Y GESTIONAR LAS OPCIONES SELECCIONADAS POR EL USUARIO.
# =================================================================================================================

"""INTERFAZ DEL USUARIO Y CONTROL DEL PROGRAMA"""

from servicios import * # IMPORTA LAS FUNCIONES DE servicios.py PARA MANEJAR EL inventario.
from archivos import * # IMPORTA LAS FUNCIONES DE archivos.py PARA GUARDAR Y CARGAR EL inventario.

# =================================================================================================================
# FUNCIONES DE VALIDACIÓN
# =================================================================================================================

def pedir_texto(mensaje): 
    """SOLICITA TEXTO NO VACÍO"""

    repetir = True # VARIABLE DE CONTROL PARA EL BUCLE DE REPETICIÓN.
    while repetir: # BUCLE QUE SE REPITE HASTA QUE EL USUARIO INGRESE UN TEXTO VÁLIDO.

        # SOLICITA TEXTO AL USUARIO.
        texto = input(mensaje).strip() # .strip() ELIMINA ESPACIOS EN BLANCO AL PRINCIPIO | FINAL.


        if texto == "": # SI EL TEXTO ESTA VACÍO MUETSRA UN MENSAJE.
            print("ERROR! NO PUEDE ESTAR VACÍO") # MENSAJE PARA EL USUARIO.
        else:
            repetir = False # CAMBIO LA VARIABLE DE CONTROL A False PARA SALIR DEL BUCLE.

    return texto # RETORNO EL TEXTO INGRESADO POR EL USUARIO A LA FUNCIÓN QUE LO LLAMÓ.


def pedir_float(mensaje):
    """SOLICITA NÚMERO DECIMAL"""

    repetir = True # VARIABLE DE CONTROL PARA EL BUCLE DE REPETICIÓN.
    while repetir: # BUCLE QUE SE REPITE HASTA QUE EL USUARIO INGRESE UN NÚMERO DECIMAL VÁLIDO.

        try:
            valor = float(input(mensaje)) # SOLICITA UN NÚMERO DECIMAL AL USUARIO.
            if valor < 0:  # SI EL NÚMERO ES NEGATIVO MUESTRA UN MENSAJE DE ERROR.
                print("EL NÚMERO NO PUEDE SER NEGATIVO") # MENSAJE PARA EL USUARIO.
            else:
                repetir = False # CAMBIO LA VARIABLE DE CONTROL A False PARA SALIR DEL BUCLE.
        except ValueError: # SI EL USUARIO INGRESA UN VALOR QUE NO ES UN NÚMERO DECIMAL MUESTRA UN MENSAJE DE ERROR.
            print("NÚMERO INVÁLIDO") # MENSAJE PARA EL USUARIO.

    return valor # RETORNO EL NÚMERO DECIMAL INGRESADO POR EL USUARIO A LA FUNCIÓN QUE LO LLAMÓ.


def pedir_int(mensaje):
    """SOLICITA NÚMERO ENTERO"""

    repetir = True # VARIABLE DE CONTROL PARA EL BUCLE DE REPETICIÓN.
    while repetir:  # BUCLE QUE SE REPITE HASTA QUE EL USUARIO INGRESE UN NÚMERO ENTEROVÁLIDO.

        try:
            valor = int(input(mensaje)) # SOLICITA UN NÚMERO ENTERO AL USUARIO.
            if valor < 0: # SI EL NÚMERO ES NEGATIVO MUESTRA UN MENSAJE DE ERROR.
                print("EL NÚMERO NO PUEDE SER NEGATIVO!") # MENSAJE PARA EL USUARIO.
            else:
                repetir = False # CAMBIO LA VARIABLE DE CONTROL A False PARA SALIR DEL BUCLE.
        except ValueError: # SI EL USUARIO INGRESA UN VALOR QUE NO ES UN NÚMERO ENTERO MUESTRA UN MENSAJE DE ERROR.
            print("NÚMERO INVÁLIDO") # MENSAJE PARA EL USUARIO.

    return valor # RETORNO EL NÚMERO ENTERO INGRESADO POR EL USUARIO A LA FUNCIÓN QUE LO LLAMÓ.

# =================================================================================================================
# FUNCIONES DE OPCIONES
# =================================================================================================================
def opcion_agregar(inventario):
    """AGREGA PRODUCTOS CON REPETICIÓN"""

    repetir = True
    while repetir:

        nombre = pedir_texto("Nombre: ")
        precio = pedir_float("Precio: ")
        cantidad = pedir_int("Cantidad: ")

        agregar_producto(inventario, nombre, precio, cantidad)
        print("✅ AGREGADO")

        respuesta = input("¿AGREGAR OTRO? (S/N): ").lower()

        if respuesta == "n":
            repetir = False


def opcion_mostrar(inventario): # PASO inventario COMO PARÁMETRO PARA EVITAR VARIABLES GLOBALES.
    """MUESTRA EL INVENTARIO"""

    if not inventario: # SI EL INVENTARIO ESTA VACIO MUESTRA UN MENSAJE.
        print("INVENTARIO VACÍO!") # MENSAJE PARA EL USUARIO.
    else:
        mostrar_inventario(inventario) # LLAMA LA FUNCIOM mostrar_inventario()


def opcion_buscar(inventario):
    """BUSCA HASTA ENCONTRAR"""

    encontrado = False # VARIABLE DE CONTROL PARA EL BUCLE DE BUSQUEDA.
    while not encontrado: # BUCLE.

        nombre = pedir_texto("Buscar: ")
        producto = buscar_producto(inventario, nombre)

        if producto:
            print("✅ ENCONTRADO:", producto)
            encontrado = True
        else:
            print("EL PRODUCTO NO EXISTE DENTRO DEL INVENTARIO!")


def opcion_actualizar(inventario):
    """ACTUALIZA CON REPETICIÓN"""

    repetir = True
    while repetir:

        nombre = pedir_texto("Producto: ")

        if not buscar_producto(inventario, nombre):
            print("❌ NO EXISTE")
        else:
            precio = input("Nuevo precio: ")
            cantidad = input("Nueva cantidad: ")

            nuevo_precio = float(precio) if precio else None
            nueva_cantidad = int(cantidad) if cantidad else None

            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            print("✅ ACTUALIZADO")

            respuesta = input("¿ACTUALIZAR OTRO? (S/N): ").lower()

            if respuesta == "n":
                repetir = False


def opcion_eliminar(inventario):
    """ELIMINA HASTA ENCONTRAR"""

    eliminado = False
    while not eliminado:

        nombre = pedir_texto("Eliminar: ")

        if eliminar_producto(inventario, nombre):
            print("✅ ELIMINADO")
            eliminado = True
        else:
            print("❌ NO EXISTE")


def opcion_estadisticas(inventario):
    """MUESTRA ESTADÍSTICAS"""

    stats = calcular_estadisticas(inventario)

    if not stats:
        print("⚠️ VACÍO")
    else:
        print("\n--- ESTADÍSTICAS ---")
        print(f"UNIDADES: {stats['unidades_totales']} ({', '.join(stats['productos'])})")
        print(f"VALOR: ${stats['valor_total']:.2f}")
        print(f"MÁS CARO: {stats['producto_mas_caro']['nombre']}")
        print(f"MAYOR STOCK: {stats['producto_mayor_stock']['nombre']}")


def opcion_guardar(inventario):
    """GUARDA ARCHIVO"""
    ruta = pedir_texto("Ruta: ")
    guardar_csv(inventario, ruta)


def opcion_cargar(inventario):
    """CARGA ARCHIVO"""

    ruta = pedir_texto("Ruta: ")
    datos = cargar_csv(ruta)

    if datos:
        inventario.clear()
        inventario.extend(datos)
        print("INVENTARIO ACTUALIZADO!")

# =================================================================================================================
# FUNCIÓN PRINCIPAL: ejecutar_menu() | CONTROLA EL CICLO PRINCIPAL DEL PROGRAMA.
# MUESTRA EL MENÚ Y PERMITE AL USUARIO INTERACTUAR HASTA QUE DECIDA SALIR.
# =================================================================================================================
def ejecutar_menu():
    """EJECUTA EL MENÚ PRINCIPAL"""
    inventario = [] # LISTA PRINCIPAL DONDE SE ALMACENAN LOS PRODUCTOS INICIALMENTE VACIA.
    
    repetir_menu = True  # VARIABLE DE CONTROL PARA EL CICLO PRINCIPAL.
    while repetir_menu: # BUCLE PRINCIPAL DEL PROGRAMA.

        # =========================================================================================================
        # MENÚ DE OPCIONES DISPONIBLES (INTERFAZ DE USUARIO)
        # =========================================================================================================
        print("\n||||| MENÚ DE INVENTARIO |||||")
        print("\n1. AGREGAR PRODUCTO")
        print("2. MOSTRAR INVENTARIO")
        print("3. BUSCAR PRODUCTO")
        print("4. ACTUALIZAR PRODUCTO")
        print("5. ELIMINAR PRODUCTO")
        print("6. VER ESTADÍSTICAS")
        print("7. GUARDAR INVENTARIO (CSV)")
        print("8. CARGAR INVENTARIO (CSV)")
        print("9. SALIR")

        # SOLICITA LA OPCIÓN AL USUARIO Y LA VALIDA.
        opcion = input("\nSELECCIONE UNA OPCIÓN: ").strip() # .strip() ELIMINA ESPACIOS EN BLANCO AL PRINCIPIO | FINAL.

        # =========================================================================================================
        # ESTRUCTURA CONDICIONAL, PARA CONTROLAR EL FLUJO CADA OPCIÓN LLAMA A UNA FUNCIÓN DIFERENTE
        # =========================================================================================================
        if opcion == "1":
            opcion_agregar(inventario)

        elif opcion == "2":
            opcion_mostrar(inventario)

        elif opcion == "3":
            opcion_buscar(inventario)

        elif opcion == "4":
            opcion_actualizar(inventario)

        elif opcion == "5":
            opcion_eliminar(inventario)

        elif opcion == "6":
            opcion_estadisticas(inventario)

        elif opcion == "7":
            opcion_guardar(inventario)

        elif opcion == "8": 
            opcion_cargar(inventario) 

        elif opcion == "9":
            print("\nGRACIAS POR USAR EL SISTEMA DE INVENTARIO, ¡HASTA PRONTO!") # MENSAJE DE DESPEDIDA PARA EL USUARIO.
            print("\n") # ESPACIO EN BLANCO PARA MEJORAR LA LECTURA.

            repetir_menu = False # CAMBIO LA VARIABLE DE CONTROL A False PARA SALIR DEL BUCLE Y TERMINAR EL PROGRAMA.

        else:
            print("\nOPCIÓN INVÁLIDA! SELECCIONE UN NÚMERO DEL 1 AL 9.") # MENSAJE DE ERROR PARA OPCIONES NO VÁLIDAS.


