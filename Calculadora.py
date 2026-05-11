# Este es el código de las funciones básicas de una calculadora

import math
import os

class Calculadora:
    def __init__(self, nombre : str = "Calculadora", version__sistema: float = 1.0):
        self.nombre             = nombre
        self.version_sistema    = version__sistema

    def Suma(self, a : float = 0, b : float = 0):
        if (math.isnan(a) or math.isnan(b)):
            raise ValueError("a y b no puede ser nan: not a number")
        else:
            return a + b

    def Resta(self, a : float = 0, b : float = 0):
        if (math.isnan(a) or math.isnan(b)):
            raise ValueError("a y b no puede ser nan: not a number")
        else:
            return a - b

    def Producto(self, a : float = 0, b : float = 0):
        if (math.isnan(a) or math.isnan(b)):
            raise ValueError("a y b no puede ser nan: not a number")
        else:
            return a * b

    def Division(self, a : float = 0, b : float = 1):
        if (b == 0):
            raise ValueError("b no puede ser 0")
        if (math.isnan(a) or math.isnan(b)):
            raise ValueError("a y b no puede ser nan: not a number")
        else:
            return a / b
        
    def Potencia_2(self, a : float = 0):
        if (math.isnan(a) ):
            raise ValueError("a  no puede ser nan: not a number")
        else:
            return a ** 2
        
    def Potencia_n(self, a : float = 0, n : float = 1):
        if (math.isnan(a) or math.isnan(n)):
            raise ValueError("a y b no puede ser nan: not a number")
        else:
            return a ** n
        
    def Raiz_cuadrada(self, a : float = 0):
        if (math.isnan(a)):
            raise ValueError("a no puede ser nan: not a number")
        if (a < 0):
            raise ValueError("a debe de ser un número positivo")
        else:
            return math.sqrt(a)
        
if __name__ == "__main__":

    calc = Calculadora("Calculadora de Randy")
    
    a = 10.0
    b = 15.0
    c = 25.0
    n = 5

    sum = calc.Suma(a,b)
    res = calc.Resta(a,b)
    pro = calc.Producto(a,b)
    div = calc.Division(a,b)
    a_2 = calc.Potencia_2(a)
    a_n = calc.Potencia_n(a,n)
    c_raiz = calc.Raiz_cuadrada(c)

    print("Los resultados son: ")
    print("Suma de %.2f y %.2f es: %.2f" % (a, b, sum))
    print("Resta de %.2f y %.2f es: %.2f" % (a, b, res))
    print("Producto de %.2f y %.2f es: %.2f" % (a, b, pro))
    print("Division de %.2f y %.2f es: %.2f"% (a, b, div))
    print("Potencia de %.2f a la 2 es: %.2f"% (a,a_2))
    print("Potencia de %.2f a la %.2f es: %.2f"% (a,n,a_n))
    print("Raiz cuadrada de %.2f es: %.2f"% (c,c_raiz))