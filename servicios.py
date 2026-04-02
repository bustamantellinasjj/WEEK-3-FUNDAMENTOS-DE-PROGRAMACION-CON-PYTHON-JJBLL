# =====================================================================================================
# MÓDULO: servicios.py | CONTIENE LA LÓGICA DEL INVENTARIO | NO INTERACTÚA CON EL USUARIO DIRECTAMENTE.
# =====================================================================================================

"""CONTIENTE LA LÓGICA DEL INVENTARIO"""
# =====================================================================================================
# FUNCIÓN: agregar_producto() | AGREGA UN NUEVO PRODUCTO A LA LISTA inventario.
# =====================================================================================================
# OPCION 1 (OK)
def agregar_producto(inventario, nombre, precio, cantidad):
    """AGREGA UN PRODUCTO AL INVENTARIO"""
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


# OPCION 2 (OK)
def mostrar_inventario(inventario):
    """MUESTRA LOS PRODUCTOS EN FORMATO DE TABLA"""
    print("-" * 50)
    print("           STOCK DE INVENTARIO       ")
    print("-" * 50)

    # ENCABEZADOS ALINEADOS
    print(f"{'Producto':<15} {'Precio':<15} {'Cantidad':<10}") # :<15 ALINEA A LA IZQUIERDA EN UN ESPACIO DE 15 CARACTERES.
    print("-" * 50)

    # RECORRE CADA PRODUCTO
    for p in inventario:
        print(f"{p['nombre']:<15} ${p['precio']:<14.2f} {p['cantidad']:<10}")
        print("-" * 50)


# OPCION 3 (OK)
def buscar_producto(inventario, nombre):
    """BUSCA UN PRODUCTO POR SU NOMBRE"""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


# OPCION 4
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """ACTUALIZA PRECIO Y/O CANTIDAD DE UN PRODUCTO"""
    producto = buscar_producto(inventario, nombre)

    if producto:
        # ACTUALIZA SI SE PROPORCIONA UN VALOR
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio

        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad

        return True

    return False

# OPCION 5
def eliminar_producto(inventario, nombre):
    """ELIMINA UN PRODUCTO DEL INVENTARIO"""
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        return True

    return False


# OPCION 6 (OK)
def calcular_estadisticas(inventario):
    """CALCULA ESTADÍSTICAS DEL INVENTARIO"""

    if not inventario:
        print("-" * 50)
        print("NO HAY PRODUCTOS EN EL INVENTARIO     ")
        print("-" * 50)
        return

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("-" * 50)
    print("        ESTADÍSTICAS DEL INVENTARIO       ")
    print("-" * 50)

    print(f"{'Unidades totales:':<25} {unidades_totales}")
    print(f"{'Valor total ($):':<25} ${valor_total:.2f}")

    print("-" * 50)
    print(f"{'Producto más caro:':<25} {producto_mas_caro['nombre']}")
    print(f"{'Precio:':<25} ${producto_mas_caro['precio']:.2f}")
    print("-" * 50)

    print(f"{'Mayor stock:':<25} {producto_mayor_stock['nombre']}")
    print(f"{'Cantidad:':<25} {producto_mayor_stock['cantidad']}")
    print("-" * 50)

    print("LISTA DE PRODUCTOS:")
    print("-" * 50)

    for p in inventario:
        print(f"{p['nombre']:<25}")
    print("-" * 50)