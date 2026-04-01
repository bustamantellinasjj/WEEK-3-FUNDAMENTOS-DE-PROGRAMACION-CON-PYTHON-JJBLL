# MÓDULO: archivos.py
"""MANEJO DE ARCHIVOS CSV PARA GUARDAR Y CARGAR EL INVENTARIO"""

import csv


def guardar_csv(inventario, ruta):
    """
    GUARDA EL INVENTARIO EN UN ARCHIVO CSV
    """
    if not inventario:
        print("⚠️ INVENTARIO VACÍO")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()
            writer.writerows(inventario)

        print(f"✅ GUARDADO EN {ruta}")

    except Exception as e:
        print(f"❌ ERROR: {e}")


def cargar_csv(ruta):
    """
    CARGA DATOS DESDE UN CSV
    """
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
                    print("⚠️ FILA INVÁLIDA IGNORADA")

        print("✅ DATOS CARGADOS")
        return inventario

    except FileNotFoundError:
        print("❌ ARCHIVO NO ENCONTRADO")

    return []