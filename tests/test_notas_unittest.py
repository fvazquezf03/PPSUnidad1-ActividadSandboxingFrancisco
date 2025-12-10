# test_notas_unittest.py
import unittest
import pytest
from notas import agregar_nota, limpiar_datos

# ----------------------------------------------------------------------
# CLASE DE PRUEBAS
# ----------------------------------------------------------------------

class TestAgregarNota(unittest.TestCase):

    def setUp(self):
        """Prepara el entorno limpiando los datos antes de cada prueba."""
        limpiar_datos()

    # ======================================================================
    # CAJA NEGRA: Pruebas de Clase de Equivalencia (CE) y Valores Límite (VL)
    # ======================================================================

    # --- Pruebas de 'nombre' (CE/VL) ---

    def test_nombre_ce1_valido_nuevo(self):
        """[CAJA NEGRA: CE1/CB4] Nombre válido que no existe (Crea alumno)."""
        resultado = agregar_nota("Alicia", 7.0)
        self.assertEqual(len(resultado), 1)

    def test_nombre_ce1_valido_existente(self):
        """[CAJA NEGRA: CE1/CB3] Nombre válido que ya existe (Añade nota)."""
        agregar_nota("Beto", 5.0)
        resultado = agregar_nota("Beto", 8.0)
        self.assertEqual(len(resultado), 2)
        
    def test_nombre_ce2_vl1_vacio(self):
        """[CAJA NEGRA: CE2/VL1] Nombre es la cadena vacía "". Se acepta."""
        resultado = agregar_nota("", 6.0)
        self.assertEqual(len(resultado), 1)
        
    def test_nombre_vl2_largo(self):
        """[CAJA NEGRA: VL2] Nombre muy largo (ej. 256 caracteres)."""
        nombre_largo = "X" * 256
        resultado = agregar_nota(nombre_largo, 9.0)
        self.assertEqual(len(resultado), 1)

    # Nota: CE3 de 'nombre' (no string) se incluye en la prueba de Caja Blanca (CB4).

    # --- Pruebas de 'nota' (CE/VL) ---

    def test_nota_ce1_vl1_valido_minimo(self):
        """[CAJA NEGRA: CE1/VL1] Nota límite válida (0)."""
        resultado = agregar_nota("VLMín", 0)
        self.assertEqual(resultado[0], 0)

    def test_nota_ce1_vl3_valido_maximo(self):
        """[CAJA NEGRA: CE1/VL3] Nota límite válida (10)."""
        resultado = agregar_nota("VLMax", 10.0)
        self.assertEqual(resultado[0], 10.0)
        
    def test_nota_ce1_vl5_decimal(self):
        """[CAJA NEGRA: CE1/VL5] Nota válida con decimales (float)."""
        resultado = agregar_nota("Decimal", 5.5)
        self.assertEqual(resultado[0], 5.5)

    def test_nota_ce2_vl2_invalido_minimo(self):
        """[CAJA NEGRA: CE2/VL2] Nota justo debajo del límite (inválida)."""
        with self.assertRaises(ValueError) as cm:
            agregar_nota("MinInv", -0.0001)
        self.assertIn("entre 0 y 10", str(cm.exception))

    def test_nota_ce3_vl4_invalido_maximo(self):
        """[CAJA NEGRA: CE3/VL4] Nota justo por encima del límite (inválida)."""
        with self.assertRaises(ValueError) as cm:
            agregar_nota("MaxInv", 10.0001)
        self.assertIn("entre 0 y 10", str(cm.exception))

    def test_nota_ce4_vl6_no_numerica(self):
        """[CAJA NEGRA: CE4/VL6] Nota no numérica (string)."""
        with self.assertRaises(ValueError) as cm:
            agregar_nota("NoNum", "5.0") # VL6
        self.assertIn("debe ser un número", str(cm.exception))
        
    # ======================================================================
    # CAJA BLANCA: Pruebas de Cobertura de Caminos Básicos (CB)
    # ======================================================================
    
    def test_cb1_nota_no_numerica(self):
        """[CAJA BLANCA: CB1] Camino 1: Nota no numérica (ej. booleano)."""
        agregar_nota("CB1", True)

    def test_cb2_nota_fuera_de_rango(self):
        """[CAJA BLANCA: CB2] Camino 2: Nota numérica fuera de rango (ej. 15)."""
        with self.assertRaises(ValueError) as cm:
            agregar_nota("CB2", 15)
        self.assertIn("entre 0 y 10", str(cm.exception))

    def test_cb3_alumno_existe_nota_valida(self):
        """[CAJA BLANCA: CB3] Camino 3: Nota válida y alumno ya existe."""
        # Precondición: El alumno existe (IF nombre not in notas es FALSE)
        agregar_nota("CB3", 5.0)
        # Ejecución del camino
        resultado = agregar_nota("CB3", 6.0)
        self.assertEqual(len(resultado), 2)
    
    def test_cb4_alumno_no_existe_nota_valida(self):
        """[CAJA BLANCA: CB4 / CE3] Camino 4: Nota válida y alumno NO existe. Incluye CE3 de 'nombre'."""
        # Precondición: El alumno NO existe (IF nombre not in notas es TRUE)
        # Usamos un caso de borde de nombre (CE3: int como nombre, si es aceptado)
        resultado = agregar_nota(12345, 7.0)
        self.assertEqual(len(resultado), 1)

if __name__ == '__main__':
    unittest.main()