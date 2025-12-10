# test_notas_pytest.py
import pytest
from notas import agregar_nota, limpiar_datos


# ======================================================================
# CAJA NEGRA: Parametrización de Clases de Equivalencia (CE) y Valores Límite (VL)
# ======================================================================

# Datos de prueba válidos para nombre y nota (CE1, VL1, VL3, VL5)
datos_validos = [
    ("CE1/VL1", "Alumno Cero", 0),      # VL1: Mínimo (Válido)
    ("CE1/VL3", "Alumno Diez", 10.0),    # VL3: Máximo (Válido)
    ("CE1/VL5", "Alumno Float", 4.5),    # VL5: Punto Flotante
    ("CE2/VL1", "", 7.0),               # VL1: Nombre vacío
    ("VL2", "X" * 256, 8.0),            # VL2: Nombre muy largo
]
@pytest.mark.parametrize("id_prueba, nombre, nota", datos_validos)
def test_caja_negra_validos(id_prueba, nombre, nota):
    """Prueba de valores y límites válidos (CE1/VL)."""
    resultado = agregar_nota(nombre, nota)
    assert len(resultado) == 1
    assert nota in resultado

# Datos de prueba inválidos para nota (CE2, CE3, CE4, VL2, VL4, VL6)
datos_invalidos_nota = [
    ("CE2/VL2", "Bajo", -0.0001, "entre 0 y 10"),   # VL2: Justo debajo del mínimo
    ("CE3/VL4", "Alto", 10.0001, "entre 0 y 10"),   # VL4: Justo por encima del máximo
    ("CE4/VL6", "NoNum", "5.0", "debe ser un número"), # VL6: Cadena no numérica
    ("CE4", "Bool", True, "debe ser un número"),      # CE4: Booleano
]
@pytest.mark.parametrize("id_prueba, nombre, nota, mensaje_esperado", datos_invalidos_nota)
def test_caja_negra_nota_invalidos(id_prueba, nombre, nota, mensaje_esperado):
    """Prueba de valores y tipos inválidos de nota."""
    with pytest.raises(ValueError) as excinfo:
        agregar_nota(nombre, nota)
    assert mensaje_esperado in str(excinfo.value)

# Datos de prueba para nombre no string (CE3 de nombre)
datos_invalidos_nombre = [
    ("CE3", 12345, 7.0),  # Entero como nombre
    ("CE3", None, 8.0),   # None como nombre
]
@pytest.mark.parametrize("id_prueba, nombre, nota", datos_invalidos_nombre)
def test_caja_negra_nombre_no_string(id_prueba, nombre, nota):
    """[CAJA NEGRA: CE3] Prueba de tipos no string en nombre (comportamiento por defecto del dict)."""
    # Si la función no tiene validación, debe aceptarlo como clave de dict.
    resultado = agregar_nota(nombre, nota)
    assert len(resultado) == 1
    assert nota in resultado

# ======================================================================
# CAJA BLANCA: Cobertura de Caminos Básicos (CB)
# ======================================================================

def test_cb1_nota_no_numerica():
    """[CAJA BLANCA: CB1] Cubre camino 1 (IF not isinstance...)."""
    with pytest.raises(ValueError):
        agregar_nota("CB1", [1, 2])

def test_cb2_nota_fuera_de_rango():
    """[CAJA BLANCA: CB2] Cubre camino 2 (IF nota < 0 or nota > 10)."""
    with pytest.raises(ValueError):
        agregar_nota("CB2", -5)

def test_cb3_alumno_existe_nota_valida():
    """[CAJA BLANCA: CB3] Cubre camino 3 (IF nombre not in notas es FALSE)."""
    # Precondición: Alumno ya existe con una nota
    agregar_nota("CB3", 5.0)  
    resultado = agregar_nota("CB3", 6.0)
    assert len(resultado) == 2

def test_cb4_alumno_no_existe_nota_valida():
    """[CAJA BLANCA: CB4] Cubre camino 4 (IF nombre not in notas es TRUE)."""
    # Precondición: Alumno no existe (El fixture ya limpió el diccionario)
    resultado = agregar_nota("CB4", 7.0)
    assert len(resultado) == 1
