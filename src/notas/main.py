"""
main.py - Punto de entrada del programa

Permite ejecutar el gestor de notas desde la línea de comandos.
"""

from notas import agregar_nota, promedio_alumno, mejor_alumno

def menu():
    print("=== Gestor de Notas ===")
    print("1. Agregar nota")
    print("2. Mostrar promedio")
    print("3. Mostrar mejor alumno")
    print("4. Salir")

def main():
    # Usamos las funciones del módulo 'notas' para consultar y mostrar datos.
    # Evitamos mantener un diccionario local que se desincroniza con el módulo.
    while True:
        menu()
        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del alumno: ")
                nota = float(input("Nota: "))
                lista = agregar_nota(nombre, nota)
                print(f"Nota {nota} agregada a {nombre}. Notas: {lista}")

            elif opcion == "2":
                nombre = input("Nombre del alumno: ")
                try:
                    media = promedio_alumno(nombre)
                    print(f"Promedio de {nombre}: {media:.2f}")
                except KeyError:
                    print("No hay notas registradas para ese alumno.")

            elif opcion == "3":
                try:
                    mejor = mejor_alumno()
                    # pedir la media para mostrarla
                    media_mejor = promedio_alumno(mejor)
                    print(f"El mejor alumno es {mejor} con media {media_mejor:.2f}")
                except ValueError:
                    print("No hay alumnos registrados.")

            elif opcion == "4":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
