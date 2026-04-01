# Sistema de Inventario en Python

Aplicación de consola desarrollada en Python que permite gestionar un inventario de productos mediante operaciones CRUD, cálculo de estadísticas y almacenamiento en archivos CSV.

---

## Características

* Agregar productos
* Mostrar inventario en formato tabla
* Buscar productos por nombre
* Actualizar precio y cantidad
* Eliminar productos
* Calcular estadísticas del inventario:

  * Valor total
  * Total de unidades
  * Producto más caro
  * Producto con mayor stock
* Guardar inventario en archivo CSV
* Cargar inventario desde archivo CSV

---

## Conceptos aplicados

Este proyecto fue desarrollado aplicando fundamentos clave de programación en Python:

* Estructuras de control (`if`, `while`)
* Funciones y modularidad
* Listas y diccionarios
* Manejo de errores (`try/except`)
* Lectura y escritura de archivos CSV
* Separación de responsabilidades (arquitectura modular)

---

## Estructura del proyecto

```bash
proyecto/
│
├── app.py          # Punto de entrada del programa
├── menu.py         # Interfaz de usuario y flujo del sistema
├── servicios.py    # Lógica del inventario
├── archivos.py     # Manejo de archivos CSV
└── README.md       # Documentación del proyecto
```

---

## Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

2. Accede a la carpeta:

```bash
cd tu-repositorio
```

3. Ejecuta el programa:

```bash
python app.py
```

---

## Ejemplo de uso

```text
||||| MENÚ DE INVENTARIO |||||

1. AGREGAR PRODUCTO
2. MOSTRAR INVENTARIO
3. BUSCAR PRODUCTO
4. ACTUALIZAR PRODUCTO
5. ELIMINAR PRODUCTO
6. VER ESTADÍSTICAS
7. GUARDAR INVENTARIO (CSV)
8. CARGAR INVENTARIO (CSV)
9. SALIR
```

---

## Tecnologías utilizadas

* Python 3

---

## Estado del proyecto

Finalizado — Proyecto funcional y estructurado bajo buenas prácticas básicas de programación.

---

## Autor

Desarrollado por **Juan José Bustamante**
Proyecto académico — Fundamentos de Programación con Python

---

## Notas

Este proyecto tiene fines educativos y busca reforzar el uso de estructuras básicas de programación, organización de código y lógica aplicada en Python.
