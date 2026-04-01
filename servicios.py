# =====================================================================================================
# MÓDULO: servicios.py | CONTIENE LA LÓGICA DEL INVENTARIO | NO INTERACTÚA CON EL USUARIO DIRECTAMENTE.
# =====================================================================================================

"""CONTIENTE LA LÓGICA DEL INVENTARIO"""
# =====================================================================================================
# FUNCIÓN: agregar_producto() | AGREGA UN NUEVO PRODUCTO A LA LISTA inventario.
# =====================================================================================================
def agregar_producto(inventario, nombre, precio, cantidad):
    """AGREGA UN PRODUCTO AL INVENTARIO"""
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """MUESTRA LOS PRODUCTOS EN FORMATO DE TABLA"""
    print("-" * 35)
    print("\n        STOCK DE INVENTARIO       ")
    print("-" * 35)
    print(f"\n{'Producto':<15} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 35)

    # RECORRE CADA PRODUCTO
    for p in inventario:
        print(f"{p['nombre']:<15} ${p['precio']:.2f}      {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """BUSCA UN PRODUCTO POR SU NOMBRE"""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


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


def eliminar_producto(inventario, nombre):
    """ELIMINA UN PRODUCTO DEL INVENTARIO"""
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        return True

    return False


def calcular_estadisticas(inventario):
    """CALCULA ESTADÍSTICAS DEL INVENTARIO"""
    if not inventario:
        return {}

    unidades_totales = sum(p["cantidad"] for p in inventario) # SUMA TOTAL DE UNIDADES EXISTENTES EN EL INVENTARIO

    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario) # SUMA TOTAL DE VALOR DE TODOS LOS PRODUCTOSDEL INVENTARIO.

    producto_mas_caro = max(inventario, key=lambda p: p["precio"]) # PRODUCTO MÁS CARO.

    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"]) # PRODUCTO CON MAYOR STOCK.

    nombres = [p["nombre"] for p in inventario] # LISTA DE NOMBRES DE PRODUCTOS.

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock,
        "productos": nombres
    }
