from Calculadora import Calculadora
import unittest
import math

class Prueba_Calculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora("Calculadora de Prueba", 1.0)
        return super().setUp()

    # ====================================================================
    # ==================== PRUEBAS PARA SUMA (1) =========================
    # ====================================================================
        
    def test_01_suma_positivos(self):
        print("\n=========== SUMA ============")
        print("----- Caso 1: Suma de dos numeros positivos -----")
        a, b = 10.5, 20.3
        print(f"Operacion: {a} + {b}")
        resultado = self.calc.Suma(a, b)
        print(f"Resultado esperado: {a + b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertAlmostEqual(resultado, a + b, places=2)
        print("OK")

    def test_02_suma_negativos(self):
        print("\n=========== SUMA ============")
        print("----- Caso 2: Suma de numeros negativos -----")
        a, b = -5.0, -3.0
        print(f"Operacion: {a} + {b}")
        resultado = self.calc.Suma(a, b)
        print(f"Resultado esperado: {a + b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a + b)
        print("OK")

    def test_03_suma_cero(self):
        print("\n=========== SUMA ============")
        print("----- Caso 3: Suma con cero -----")
        a, b = 0.0, 7.0
        print(f"Operacion: {a} + {b}")
        resultado = self.calc.Suma(a, b)
        print(f"Resultado esperado: {a + b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a + b)
        print("OK")

    def test_04_suma_nan(self):
        print("\n=========== SUMA ============")
        print("----- Caso 4: Suma con NaN (debe lanzar ValueError) -----")
        a, b = float('nan'), 5.0
        print(f"Operacion: {a} + {b}")
        print("Resultado esperado: ValueError (no se puede sumar NaN)")
        with self.assertRaises(ValueError):
            self.calc.Suma(a, b)
        print("OK - Excepcion ValueError capturada correctamente")

    def test_05_suma_grandes(self):
        print("\n=========== SUMA ============")
        print("----- Caso 5: Numeros muy grandes (limite de float) -----")
        a, b = 1e308, 1e308
        print(f"Operacion: {a} + {b}")
        resultado = self.calc.Suma(a, b)
        print(f"Resultado esperado: inf (overflow)")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, float('inf'))
        print("OK")

    # ====================================================================
    # ==================== PRUEBAS PARA RESTA (2) ========================
    # ====================================================================
    
    def test_06_resta_positivos(self):
        print("\n=========== RESTA ============")
        print("----- Caso 1: Resta basica con resultado positivo -----")
        a, b = 15.0, 4.0
        print(f"Operacion: {a} - {b}")
        resultado = self.calc.Resta(a, b)
        print(f"Resultado esperado: {a - b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a - b)
        print("OK")

    def test_07_resta_negativos(self):
        print("\n=========== RESTA ============")
        print("----- Caso 2: Resta que da negativo -----")
        a, b = 3.0, 10.0
        print(f"Operacion: {a} - {b}")
        resultado = self.calc.Resta(a, b)
        print(f"Resultado esperado: {a - b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a - b)
        print("OK")

    def test_08_resta_cero(self):
        print("\n=========== RESTA ============")
        print("----- Caso 3: Resta con cero -----")
        a, b = 0.0, 5.0
        print(f"Operacion: {a} - {b}")
        resultado = self.calc.Resta(a, b)
        print(f"Resultado esperado: {a - b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a - b)
        print("OK")

    def test_09_resta_nan(self):
        print("\n=========== RESTA ============")
        print("----- Caso 4: NaN en algun argumento -----")
        a, b = 8.0, float('nan')
        print(f"Operacion: {a} - {b}")
        print("Resultado esperado: ValueError (no se puede restar NaN)")
        with self.assertRaises(ValueError):
            self.calc.Resta(a, b)
        print("OK - Excepcion ValueError capturada correctamente")

    # ====================================================================
    # ==================== PRUEBAS PARA PRODUCTO (3) =====================
    # ====================================================================
    
    def test_10_producto_enteros(self):
        print("\n=========== PRODUCTO ============")
        print("----- Caso 1: Multiplicacion de enteros -----")
        a, b = 6, 7
        print(f"Operacion: {a} * {b}")
        resultado = self.calc.Producto(a, b)
        print(f"Resultado esperado: {a * b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a * b)
        print("OK")

    def test_11_producto_decimales(self):
        print("\n=========== PRODUCTO ============")
        print("----- Caso 2: Multiplicacion con decimales -----")
        a, b = 2.5, 1.5
        print(f"Operacion: {a} * {b}")
        resultado = self.calc.Producto(a, b)
        print(f"Resultado esperado: {a * b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertAlmostEqual(resultado, a * b, places=2)
        print("OK")

    def test_12_producto_por_cero(self):
        print("\n=========== PRODUCTO ============")
        print("----- Caso 3: Multiplicacion por cero -----")
        a, b = 100.0, 0.0
        print(f"Operacion: {a} * {b}")
        resultado = self.calc.Producto(a, b)
        print(f"Resultado esperado: {a * b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a * b)
        print("OK")

    def test_13_producto_nan(self):
        print("\n=========== PRODUCTO ============")
        print("----- Caso 4: NaN produce ValueError -----")
        a, b = float('nan'), 99.0
        print(f"Operacion: {a} * {b}")
        print("Resultado esperado: ValueError (no se puede multiplicar NaN)")
        with self.assertRaises(ValueError):
            self.calc.Producto(a, b)
        print("OK - Excepcion ValueError capturada correctamente")

    # ====================================================================
    # ==================== PRUEBAS PARA DIVISION (4) =====================
    # ====================================================================
    
    def test_14_division_exacta(self):
        print("\n=========== DIVISION ============")
        print("----- Caso 1: Division exacta entre enteros -----")
        a, b = 10, 2
        print(f"Operacion: {a} / {b}")
        resultado = self.calc.Division(a, b)
        print(f"Resultado esperado: {a / b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a / b)
        print("OK")

    def test_15_division_decimal(self):
        print("\n=========== DIVISION ============")
        print("----- Caso 2: Division con resultado decimal periodico -----")
        a, b = 1, 3
        print(f"Operacion: {a} / {b}")
        resultado = self.calc.Division(a, b)
        print(f"Resultado esperado: {a / b}")
        print(f"Resultado obtenido: {resultado}")
        self.assertAlmostEqual(resultado, a / b, places=6)
        print("OK")

    def test_16_division_por_cero(self):
        print("\n=========== DIVISION ============")
        print("----- Caso 3: Division entre cero (debe lanzar ValueError) -----")
        a, b = 5, 0
        print(f"Operacion: {a} / {b}")
        print("Resultado esperado: ValueError (no se puede dividir por cero)")
        with self.assertRaises(ValueError):
            self.calc.Division(a, b)
        print("OK - Excepcion ValueError capturada correctamente")

    def test_17_division_nan(self):
        print("\n=========== DIVISION ============")
        print("----- Caso 4: NaN en numerador o denominador -----")
        a, b = float('nan'), 4
        print(f"Operacion: {a} / {b}")
        print("Resultado esperado: ValueError (no se puede dividir NaN)")
        with self.assertRaises(ValueError):
            self.calc.Division(a, b)
        print("OK - Excepcion ValueError capturada correctamente")

    # ====================================================================
    # ==================== PRUEBAS PARA POTENCIA_2 (5) ===================
    # ====================================================================
    
    def test_18_potencia_2_entero(self):
        print("\n=========== POTENCIA_2 ============")
        print("----- Caso 1: Cuadrado de un entero positivo -----")
        a = 4
        print(f"Operacion: {a} ** 2")
        resultado = self.calc.Potencia_2(a)
        print(f"Resultado esperado: {a ** 2}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a ** 2)
        print("OK")

    def test_19_potencia_2_negativo(self):
        print("\n=========== POTENCIA_2 ============")
        print("----- Caso 2: Cuadrado de un numero negativo -----")
        a = -3
        print(f"Operacion: {a} ** 2")
        resultado = self.calc.Potencia_2(a)
        print(f"Resultado esperado: {a ** 2}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a ** 2)
        print("OK")

    def test_20_potencia_2_cero(self):
        print("\n=========== POTENCIA_2 ============")
        print("----- Caso 3: Cuadrado de cero -----")
        a = 0
        print(f"Operacion: {a} ** 2")
        resultado = self.calc.Potencia_2(a)
        print(f"Resultado esperado: {a ** 2}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a ** 2)
        print("OK")

    def test_21_potencia_2_nan(self):
        print("\n=========== POTENCIA_2 ============")
        print("----- Caso 4: NaN causa ValueError -----")
        a = float('nan')
        print(f"Operacion: {a} ** 2")
        print("Resultado esperado: ValueError (no se puede elevar NaN al cuadrado)")
        with self.assertRaises(ValueError):
            self.calc.Potencia_2(a)
        print("OK - Excepcion ValueError capturada correctamente")

    # ====================================================================
    # ==================== PRUEBAS PARA POTENCIA_N (6) ===================
    # ====================================================================
    
    def test_22_potencia_n_exponente_entero(self):
        print("\n=========== POTENCIA_N ============")
        print("----- Caso 1: Potencia con exponente entero positivo -----")
        a, n = 2, 3
        print(f"Operacion: {a} ** {n}")
        resultado = self.calc.Potencia_n(a, n)
        print(f"Resultado esperado: {a ** n}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a ** n)
        print("OK")

    def test_23_potencia_n_exponente_cero(self):
        print("\n=========== POTENCIA_N ============")
        print("----- Caso 2: Exponente cero (siempre da 1) -----")
        a, n = 5, 0
        print(f"Operacion: {a} ** {n}")
        resultado = self.calc.Potencia_n(a, n)
        print(f"Resultado esperado: {a ** n}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a ** n)
        print("OK")

    def test_24_potencia_n_base_negativa(self):
        print("\n=========== POTENCIA_N ============")
        print("----- Caso 3: Base negativa con exponente impar -----")
        a, n = -2, 3
        print(f"Operacion: {a} ** {n}")
        resultado = self.calc.Potencia_n(a, n)
        print(f"Resultado esperado: {a ** n}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, a ** n)
        print("OK")

    def test_25_potencia_n_nan(self):
        print("\n=========== POTENCIA_N ============")
        print("----- Caso 4: Argumento NaN (ValueError) -----")
        a, n = 2, float('nan')
        print(f"Operacion: {a} ** {n}")
        print("Resultado esperado: ValueError (exponente no puede ser NaN)")
        with self.assertRaises(ValueError):
            self.calc.Potencia_n(a, n)
        print("OK - Excepcion ValueError capturada correctamente")

    # ====================================================================
    # ==================== PRUEBAS PARA RAIZ_CUADRADA (7) ================
    # ====================================================================
    
    def test_26_raiz_cuadrada_positivo(self):
        print("\n=========== RAIZ_CUADRADA ============")
        print("----- Caso 1: Raiz de un numero positivo exacto -----")
        a = 25
        print(f"Operacion: sqrt({a})")
        resultado = self.calc.Raiz_cuadrada(a)
        print(f"Resultado esperado: {math.sqrt(a)}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, math.sqrt(a))
        print("OK")

    def test_27_raiz_cuadrada_decimal(self):
        print("\n=========== RAIZ_CUADRADA ============")
        print("----- Caso 2: Raiz de un numero no cuadrado perfecto -----")
        a = 2
        print(f"Operacion: sqrt({a})")
        resultado = self.calc.Raiz_cuadrada(a)
        print(f"Resultado esperado: {math.sqrt(a)}")
        print(f"Resultado obtenido: {resultado}")
        self.assertAlmostEqual(resultado, math.sqrt(a), places=6)
        print("OK")

    def test_28_raiz_cuadrada_cero(self):
        print("\n=========== RAIZ_CUADRADA ============")
        print("----- Caso 3: Raiz de cero -----")
        a = 0
        print(f"Operacion: sqrt({a})")
        resultado = self.calc.Raiz_cuadrada(a)
        print(f"Resultado esperado: {math.sqrt(a)}")
        print(f"Resultado obtenido: {resultado}")
        self.assertEqual(resultado, math.sqrt(a))
        print("OK")

    def test_29_raiz_cuadrada_negativo(self):
        print("\n=========== RAIZ_CUADRADA ============")
        print("----- Caso 4: Numero negativo (debe lanzar ValueError) -----")
        a = -4
        print(f"Operacion: sqrt({a})")
        print("Resultado esperado: ValueError (no existe raiz real de numero negativo)")
        with self.assertRaises(ValueError):
            self.calc.Raiz_cuadrada(a)
        print("OK - Excepcion ValueError capturada correctamente")

    def test_30_raiz_cuadrada_nan(self):
        print("\n=========== RAIZ_CUADRADA ============")
        print("----- Caso 5: NaN (debe lanzar ValueError) -----")
        a = float('nan')
        print(f"Operacion: sqrt({a})")
        print("Resultado esperado: ValueError (no se puede calcular raiz de NaN)")
        with self.assertRaises(ValueError):
            self.calc.Raiz_cuadrada(a)
        print("OK - Excepcion ValueError capturada correctamente")

# ====================================================================
# ==================== EJECUCION DE PRUEBAS ==========================
# ====================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("INICIANDO PRUEBAS UNITARIAS PARA CALCULADORA")
    print("="*80)
    
    # Ejecutar las pruebas
    unittest.main(verbosity=0)