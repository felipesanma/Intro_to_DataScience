# -*- coding: UTF-8 -*-
"""
Ejemplo de un módulo Python. Contiene una variable llamada mi_variable,
una función llamada mi_function, y una clase llamada MiClase.
"""

mi_variable = 0

def mi_function():
    """
    Función ejemplo
    """
    return mi_variable
    
class MiClase:
    """
    Clase ejemplo.
    """

    def __init__(self):
        self.variable = mi_variable
        
    def set_variable(self, nuevo_valor):
        """
        Asigna self.variable a un nuevo valor
        """
        self.variable = nuevo_valor
        
    def get_variable(self):
        return self.variable
