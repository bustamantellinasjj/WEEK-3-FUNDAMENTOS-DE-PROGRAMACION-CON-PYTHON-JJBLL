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

        try:
             # SOLICITA TEXTO AL USUARIO.
            texto = input(mensaje).strip() # .strip() ELIMINA ESPACIOS EN BLANCO AL PRINCIPIO | FINAL.
        except (KeyboardInterrupt, EOFError):  # CTRL+C o CTRL+Z
            print("-" * 55)
            print("\nATAJO NO PERMITIDO! INTENTE DE NUEVO.") # MENSAJE PARA EL USUARIO.
            texto = ""
        
        if texto == "": # SI EL TEXTO ESTA VACÍO MUESTRA UN MENSAJE.
            print("-" * 55)
            print("ERROR! NO PUEDE ESTAR VACÍO") # MENSAJE PARA EL USUARIO.
        else:
            repetir = False # CAMBIO LA VARIABLE DE CONTROL A False PARA SALIR DEL BUCLE.

    return texto # RETORNO EL TEXTO INGRESADO POR EL USUARIO A LA FUNCIÓN QUE LO LLAMÓ.

def pedir_float(mensaje):
    """SOLICITA NÚMERO DECIMAL"""

    repetir = True # VARIABLE DE CONTROL PARA EL BUCLE DE REPETICIÓN.
    while repetir: # BUCLE QUE SE REPITE HASTA QUE EL USUARIO INGRESE UN NÚMERO DECIMAL VÁLIDO.

        try:
            valor_texto = input(mensaje).strip() # SOLICITA UN NÚMERO DECIMAL AL USUARIO Y ELIMINA ESPACIOS EN BLANCO AL PRINCIPIO | FINAL.
        except (KeyboardInterrupt, EOFError):  # CTRL+C o CTRL+Z
            print("-" * 55)
            print("\nATAJO NO PERMITIDO! INTENTE DE NUEVO.") # MENSAJE PARA EL USUARIO.
            valor_texto = ""
        
        if valor_texto == "":
            print("-" * 55)
            print("NÚMERO INVÁLIDO") # MENSAJE PARA EL USUARIO.
            continue

        try:
            valor = float(valor_texto)
            if valor < 0:  # SI EL NÚMERO ES NEGATIVO MUESTRA UN MENSAJE DE ERROR.
                print("-" * 55)
                print("EL NÚMERO NO PUEDE SER NEGATIVO") # MENSAJE PARA EL USUARIO.
            else:
                repetir = False # CAMBIO LA VARIABLE DE CONTROL A False PARA SALIR DEL BUCLE.
        except ValueError: 
            print("-" * 55)
            print("NÚMERO INVÁLIDO") # MENSAJE PARA EL USUARIO.

    return valor

def pedir_int(mensaje):
    """SOLICITA NÚMERO ENTERO"""

    repetir = True # VARIABLE DE CONTROL PARA EL BUCLE DE REPETICIÓN.
    while repetir: # BUCLE QUE SE REPITE HASTA QUE EL USUARIO INGRESE UN NÚMERO ENTEROVÁLIDO.

        try:
            valor_texto = input(mensaje).strip() # SOLICITA UN NÚMERO ENTERO AL USUARIO.
        except (KeyboardInterrupt, EOFError):  # ENCAPSULA ERROES DE INTERRUPCION: CTRL+C | CTRL+Z
            print("-" * 55)
            print("\nATAJO NO PERMITIDO! INTENTE DE NUEVO.") # MENSAJE PARA EL USUARIO.
            valor_texto = ""
        
        if valor_texto == "":
            print("-" * 55)
            print("NÚMERO INVÁLIDO") # MENSAJE PARA EL USUARIO.
            continue

        try:
            valor = int(valor_texto) # CONVIERTO EL TEXTO INGRESADO POR EL USUARIO A UN NÚMERO ENTERO.
            if valor < 0:  # SI EL NÚMERO ES NEGATIVO MUESTRA UN MENSAJE DE ERROR.
                print("-" * 55)
                print("EL NÚMERO NO PUEDE SER NEGATIVO!") # MENSAJE PARA EL USUARIO.
            else:
                repetir = False # CAMBIO LA VARIABLE DE CONTROL A False PARA SALIR DEL BUCLE.
        except ValueError: # SI EL USUARIO INGRESA UN VALOR QUE NO ES UN NÚMERO ENTERO MUESTRA UN MENSAJE DE ERROR.
            print("-" * 55)
            print("NÚMERO INVÁLIDO") # MENSAJE PARA EL USUARIO.

    return valor # RETORNO EL NÚMERO ENTERO INGRESADO POR EL USUARIO A LA FUNCIÓN QUE LO LLAMÓ.

# =================================================================================================================
# FUNCIONES DE OPCIONES 1-8 | CADA FUNCIÓN CORRESPONDE A UNA OPCIÓN DEL MENÚ Y MANEJA LA INTERACCIÓN CON EL USUARIO PARA ESA OPCIÓN.
# =================================================================================================================
# OPCION 1 (OK)
def opcion_agregar(inventario):
    """AGREGA PRODUCTOS CON REPETICIÓN"""

    repetir = True
    while repetir:

        print("-" * 55)
        print("HAS SELECIONADO | AGREGAR PRODUCTO:") # MENSAJE PARA EL USUARIO.
        print("-" * 55)

        nombre = pedir_texto("Nombre: ") # SOLICITA EL NOMBRE DEL PRODUCTO AL USUARIO.
        precio = pedir_float("Precio: ") # SOLICITA EL PRECIO DEL PRODUCTO AL USUARIO.
        cantidad = pedir_int("Cantidad: ") # SOLICITA LA CANTIDAD DEL PRODUCTO AL USUARIO.

        agregar_producto(inventario, nombre, precio, cantidad) 
        print("-" * 55)
        print("PRODUCTO AGREGADO EXITOSAMENTE!")

        # CONTROL DE REPETICIÓN PARA AGREGAR OTRO PRODUCTO O SALIR DE LA OPCIÓN.
        respuesta = ""
        while respuesta == "":
            print("-" * 55)
            respuesta = input("¿AGREGAR OTRO? (S/N): ").strip().lower()

            if respuesta == "s":
                repetir = True

            elif respuesta == "n":
                print("-" * 55)
                repetir = False

            else:
                print("-" * 55)
                print("LETRA INVÁLIDA! ESCRIBA S/N")
                respuesta = ""

# OPCION 2 (OK)
def opcion_mostrar(inventario): # PASO inventario COMO PARÁMETRO PARA EVITAR VARIABLES GLOBALES.
    """MUESTRA EL INVENTARIO"""

    if not inventario: # SI EL INVENTARIO ESTA VACIO MUESTRA UN MENSAJE.
        print("-" * 50)
        print("ACTUALMENTE EL INVENTARIO ESTA VACÍO!") # MENSAJE PARA EL USUARIO.
        print("-" * 50)

    else:
        mostrar_inventario(inventario) # LLAMA LA FUNCIOM mostrar_inventario()


# OPCION 3 (OK)
def opcion_buscar(inventario): 
    """BUSCA PRODUCTOS CON REPETICIÓN"""

    repetir = True # VARIABLE DE CONTROL PARA EL BUCLE DE BUSQUEDA.
    while repetir: #BUCLE.

        print("-" * 55)
        print("HAS SELECCIONADO | BUSCAR PRODUCTO:") # MENSAJE PARA EL USUARIO.
        print("-" * 55)

        nombre = pedir_texto("NOMBRE DEL PRODUCTO: ") # SOLICITA EL NOMBRE DEL PRODUCTO AL USUARIO.
        producto = buscar_producto(inventario, nombre)
        
        print("-" * 55)
        if producto:

            precio = float(producto['precio']) # CONVIERTO EL PRECIO A FLOAT PARA FORMATEARLO CON 2 DECIMALES EN LA IMPRESIÓN.
            print(f"Nombre: {producto['nombre']} | Precio: {precio:.2f} | Cantidad: {producto['cantidad']}")      
        else:
            print("EL PRODUCTO NO EXISTE DENTRO DEL INVENTARIO!")

        # CONTROL DE REPETICIÓN PARA BUSCAR OTRO PRODUCTO O SALIR DE LA OPCIÓN.
        respuesta = ""
        while respuesta == "":
            print("-" * 55)
            respuesta = input("¿BUSCAR OTRO PRODUCTO? (S/N): ").strip().lower() 

            if respuesta == "s":
                repetir = True
            
            elif respuesta == "n":
                repetir = False
    
            else:
                print("LETRA INVÁLIDA! ESCRIBA S/N")
                respuesta = ""
            
# OPCION 4 (OK)
def opcion_actualizar(inventario):
    """ACTUALIZA PRECIO Y/O CANTIDAD DE UN PRODUCTO"""

    repetir = True  # VARIABLE DE CONTROL PARA EL BUCLE DE ACTUALIZACIÓN.
    while repetir:  # BUCLE QUE SE REPITE HASTA QUE EL USUARIO DECIDA NO ACTUALIZAR MÁS PRODUCTOS.

        print("-" * 55)
        print("HAS SELECCIONADO | ACTUALIZAR PRODUCTO:")  # MENSAJE PARA EL USUARIO.
        print("-" * 55)

        nombre = pedir_texto("NOMBRE DEL PRODUCTO A ACTUALIZAR: ")  # SOLICITA EL NOMBRE DEL PRODUCTO.
        producto = buscar_producto(inventario, nombre)
        print("-" * 55)

        if not producto:
            print("EL PRODUCTO NO EXISTE EN EL INVENTARIO!")  # MENSAJE PARA EL USUARIO.
        else:
            print(f"Producto encontrado: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
            print("-" * 55)

            nuevo_precio = input("NUEVO PRECIO (ENTER para mantener): ").strip()
            nueva_cantidad = input("NUEVA CANTIDAD (ENTER para mantener): ").strip()

            # VALIDAR PRECIO
            if nuevo_precio != "":
                if not nuevo_precio.replace(".", "", 1).isdigit():
                    print("EL PRECIO DEBE SER UN NÚMERO!")
                    continue
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio < 0:
                    print("EL PRECIO NO PUEDE SER MENOR QUE 0!")
                    continue
            else:
                nuevo_precio = None

            # VALIDAR CANTIDAD
            if nueva_cantidad != "":
                if not nueva_cantidad.isdigit():
                    print("LA CANTIDAD DEBE SER UN NÚMERO ENTERO!") # MENSAJE PARA EL USUARIO.
                    continue
                nueva_cantidad = int(nueva_cantidad)
                if nueva_cantidad < 0:
                    print("LA CANTIDAD NO PUEDE SER MENOR QUE 0!") # MENSAJE PARA EL USUARIO.
                    continue
            else:
                nueva_cantidad = None

            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            print("-" * 55)
            print("PRODUCTO ACTUALIZADO EXITOSAMENTE!")  # MENSAJE PARA EL USUARIO.

        # CONTROL DE REPETICIÓN PARA ACTUALIZAR OTRO PRODUCTO O SALIR DE LA OPCIÓN.
        respuesta = ""
        while respuesta == "":
            print("-" * 55)
            respuesta = input("¿ACTUALIZAR OTRO PRODUCTO? (S/N): ").strip().lower()

            if respuesta == "s":
                repetir = True
            elif respuesta == "n":
                print("-" * 55)
                repetir = False
            else:
                print("LETRA INVÁLIDA! ESCRIBA S/N")
                respuesta = ""


# OPCION 5 (OK)
def opcion_eliminar(inventario):
    """ELIMINA PRODUCTOS CON REPETICIÓN"""

    repetir = True # VARIABLE DE CONTROL PARA EL BUCLE DE ELIMINACIÓN.
    while repetir: # BUCLE QUE SE REPITE HASTA QUE EL USUARIO DECIDA NO ELIMINAR MÁS PRODUCTOS.

        print("-" * 55)
        print("HAS SELECCIONADO | ELIMINAR PRODUCTO:") # MENSAJE PARA EL USUARIO.
        print("-" * 55)

        nombre = pedir_texto("NOMBRE DEL PRODUCTO A ELIMINAR: ") # SOLICITA EL NOMBRE DEL PRODUCTO A ELIMINAR AL USUARIO.
        producto = buscar_producto(inventario, nombre) # BUSCA EL PRODUCTO EN EL INVENTARIO PARA VER SI EXISTE ANTES DE INTENTAR ELIMINARLO.

        print("-" * 55)
        if not producto:
            print("EL PRODUCTO NO EXISTE EN EL INVENTARIO!") # MENSAJE PARA EL USUARIO.
        else:
            eliminar_producto(inventario, nombre) # LLAMA LA FUNCIÓN eliminar_producto() PARA ELIMINAR EL PRODUCTO DEL INVENTARIO.
            print("PRODUCTO ELIMINADO EXITOSAMENTE!") # MENSAJE PARA EL USUARIO.
        
        # CONTROL DE REPETICIÓN PARA ELIMINAR OTRO PRODUCTO O SALIR DE LA OPCIÓN.
        respuesta = ""
        while respuesta == "":
            print("-" * 55)
            respuesta = input("¿ELIMINAR OTRO PRODUCTO? (S/N): ").strip().lower()

            if respuesta == "s":
                repetir = True

            elif respuesta == "n":
                print("-" * 55)
                repetir = False

            else:
                print("LETRA INVÁLIDA! ESCRIBA S/N") # MENSAJE PARA EL USUARIO.
                respuesta = ""


# OPCION 6: (OK)
def opcion_estadisticas(inventario):
    """MUESTRA ESTADÍSTICAS"""
    calcular_estadisticas(inventario)

   
# =================================================================================================================
# CSV: GUARDAR Y CARGAR INVENTARIO | OPCIONES 7 Y 8 DEL MENÚ.
# =================================================================================================================

# OPCION 7 | GUARDAR INVENTARIO EN UN ARCHIVO CSV. (OK)
def opcion_guardar(inventario):
    """GUARDA ARCHIVO CSV"""
    print("-" * 55)
    ruta = pedir_texto("NOMBRA LA RUTA DEL CSV: ")
    guardar_csv(inventario, ruta)

# OPCION 8 | CARGAR INVENTARIO DESDE UN ARCHIVO CSV. (OK)
def opcion_cargar(inventario): 
    """CARGA ARCHIVO"""
    print("-" * 55)
    ruta = pedir_texto("NOMBRE DE LA RUTA DEL ARCHIVO CSV A CARGAR: ") # SOLICITA LA RUTA DEL ARCHIVO CSV AL USUARIO.
    print("-" * 55)

    datos = cargar_csv(ruta)

    if datos:
        inventario.clear()
        inventario.extend(datos)
        print("INVENTARIO ACTUALIZADO!")
        print("-" * 55)
        

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