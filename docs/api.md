# Referencia de la API

## `agregar_nota(nombre, nota)`

Agrega una nota a un alumno.  
Si el alumno no existe, se crea automáticamente.

- **Parámetros:**
  - `nombre` (*str*): nombre del alumno.
  - `nota` (*float*): valor entre 0 y 10.
- **Lanza:** `ValueError` si la nota no es válida.

---

## `promedio_alumno(nombre)`

Devuelve el promedio de notas de un alumno.

- **Lanza:** `KeyError` si el alumno no existe.

---

## `mejor_alumno()`

Devuelve el nombre del alumno con la mejor media.

- **Lanza:** `ValueError` si no hay alumnos registrados.

---

## `limpiar_datos()`

Elimina todas las notas almacenadas.  
Ideal para reiniciar el sistema o usar en las pruebas unitarias.
