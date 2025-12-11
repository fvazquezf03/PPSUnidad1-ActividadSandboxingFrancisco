#!/usr/bin/env bash
# Helper para ejecutar los tests del subproyecto
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Ejecutando tests desde: $ROOT_DIR"

# Si existe pytest en PATH, úsalo. Si no, cae a python -m unittest.
if command -v pytest >/dev/null 2>&1; then
    echo "Usando pytest..."
    pytest -q
else
    echo "pytest no encontrado, usando unittest discovery en ./tests ..."
    # For reliable discovery, point explicitly to the tests directory and pattern
    python3 -m unittest discover -s tests -p "test_*.py" -v
fi
