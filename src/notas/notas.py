"""
Módulo notas.py

Contiene funciones para gestionar notas de alumnos:
- agregar_nota
- promedio_alumno
- mejor_alumno
- limpiar_datos
"""

# --- Variables globales ---
notas = {}  # Diccionario global: {nombre: [notas]}

# --- Funciones ---
def agregar_nota(nombre, nota):
    """Agrega una nota a un alumno. Crea el alumno si no existe."""
    if isinstance(nota, bool):
        raise ValueError("La nota debe ser un número")
    if not isinstance(nota, (int, float)):
        raise ValueError("La nota debe ser un número")
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10")
    if nombre not in notas:
        notas[nombre] = []
    notas[nombre].append(nota)
    return notas[nombre]

def promedio_alumno(nombre):
    """Devuelve el promedio de notas de un alumno."""
    if nombre not in notas:
        raise KeyError(f"El alumno '{nombre}' no existe")
    lista = notas[nombre]
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def mejor_alumno():
    """Devuelve el nombre del alumno con mejor promedio."""
    if not notas:
        raise ValueError("No hay alumnos registrados")
    mejor = None
    mejor_media = -1
    for nombre, lista in notas.items():
        if not lista:
            continue
        media = sum(lista) / len(lista)
        if media > mejor_media:
            mejor_media = media
            mejor = nombre
    return mejor

def limpiar_datos():
    """Vacía todas las notas (para pruebas)."""
    notas.clear()
# --- FIN Módulo notas.py ---