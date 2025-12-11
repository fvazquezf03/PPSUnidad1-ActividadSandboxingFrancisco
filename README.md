# Actividad Unidad 1 — Sandboxing (Firetools GUI)

## Índice:
1. [Proyecto](#proyecto)
2. [Descripción](#descripción)
3. [Requisitos](#requisitos)
4. [Uso rápido (Firetools)](#uso-rápido-firetools-gui)

- Enlaces para ver los documentos:
5.  [Reflexión de los lenguajes](Documentación/Reflexion_Lenguajes.md)
6.  [Guía Firetools (pasos)](Documentación/Actividad_Sandboxing_Entrega.md)


## **Proyecto:** 
Ejecución y documentación de la aplicación `nota` en un entorno aislado usando Firetools (interfaz gráfica de Firejail).

## Descripción
Repositorio con la guía para ejecutar `nota` dentro de un sandbox (Firetools) y recopilar evidencias para la entrega de la actividad.

## Requisitos
- `python3`
- `firejail` y `firetools`

```bash
sudo apt update
sudo apt install -y firejail firetools
```

## Uso rápido (Firetools GUI)
1. Abrir `Firetools`.
2. En **Command** poner: `python3 nota.py`.
3. En **Working Directory** indicar: `~/proyecto-nota`.
4. Marcar `Private mode` y, si hace falta, `Disable network` y `Whitelist` a `~/proyecto-nota`.
5. Guardar perfil y `Run`.












