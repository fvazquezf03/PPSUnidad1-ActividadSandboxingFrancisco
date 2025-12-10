"""
src/notas/__init__.py

Paquete notas

Este paquete contiene módulos relacionados con la gestión de notas de alumnos.
"""

__version__ = "0.1.0"
__author__ = "PPS"

# Importa las funciones del archivo notas.py dentro de este paquete
from .notas import agregar_nota, promedio_alumno, mejor_alumno, limpiar_datos

# Opcional: Esto permite que las funciones se accedan directamente desde el paquete 'notas'.
__all__ = ['agregar_nota', 'promedio_alumno', 'mejor_alumno', 'limpiar_datos']