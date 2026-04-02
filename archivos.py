# MÓDULO: archivos.py
"""MANEJO DE ARCHIVOS CSV PARA GUARDAR Y CARGAR EL INVENTARIO"""

import csv # IMPORTA EL MÓDULO CSV PARA GUARDAR Y CARGAR ARCHIVOS.

# OPCION 7 | GUARDAR INVENTARIO EN UN ARCHIVO CSV. (OK)
def guardar_csv(inventario, ruta):
    """GUARDA EL INVENTARIO EN UN ARCHIVO CSV"""
    if not inventario: # VERIFICA SI EL INVENTARIO ESTÁ VACÍO ANTES DE GUARDAR.
        print("-" * 50)
        print("ACTUALMENTE EL INVENTARIO ESTA VACÍO!") # MENSAJE PARA EL USUARIO.
        print("-" * 50)

        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()
            writer.writerows(inventario)
        print("-" * 50)
        print(f"GUARDADO EXITOSAMENTE EN: {ruta}")
        print("-" * 50)


    except Exception as e:
        print(f"ERROR!: {e}")

# OPCION 8 | CARGAR INVENTARIO DESDE UN ARCHIVO CSV. (OK)
def cargar_csv(ruta):
    """CARGA DATOS DESDE UN CSV"""
    inventario = []

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                try:
                    inventario.append({
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    })
                except:
                    print("FILA INVÁLIDA IGNORADA!")

        print("DATOS CARGADOS EXITOSAMENTE!")
        return inventario

    except FileNotFoundError:
        print("LA RUTA SUMINISTRADA, NO EXISTE!")
        print("-" * 47)

    return []