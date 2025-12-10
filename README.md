# BorradoraplicacionNotas — instrucciones rápidas

Pequeño subproyecto educativo con un paquete `notas` bajo `src/` y tests en `tests/`.

Pasos recomendados para desarrollo local:

1. Crear y activar un entorno virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias de desarrollo y el paquete en editable:

```bash
pip install -r requeriments.txt
pip install -e .
```

3. Ejecutar tests:

Con pytest (si está instalado):

```bash
pytest -q
```

O usando el helper incluido (usa pytest si está disponible y, si no, ejecuta unittest):

```bash
./scripts/run-tests.sh
```

4. Generar/servir la documentación (mkdocs):

```bash
mkdocs serve
```

Notas:
- Si no quieres activar el venv, puedes usar `PYTHONPATH=src python -m unittest ...` para ejecutar tests sin instalar el paquete.
- El proyecto está configurado para instalación editable (`pip install -e .`) mediante `pyproject.toml` + `setup.cfg`.
