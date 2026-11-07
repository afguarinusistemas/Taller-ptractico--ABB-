class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, actual, dato):
        if dato == actual.dato:
            return  # No se admiten duplicados

        if dato < actual.dato:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(dato)
            else:
                self._insertar_recursivo(actual.izquierdo, dato)
        else:
            if actual.derecho is None:
                actual.derecho = Nodo(dato)
            else:
                self._insertar_recursivo(actual.derecho, dato)

    def buscar(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, actual, dato):
        if actual is None:
            return False

        if actual.dato == dato:
            return True

        if dato < actual.dato:
            return self._buscar_recursivo(actual.izquierdo, dato)

        return self._buscar_recursivo(actual.derecho, dato)

    # Preorden: raíz, izquierda, derecha
    def preorden(self, actual):
        if actual is not None:
            print(actual.dato, end=" ")
            self.preorden(actual.izquierdo)
            self.preorden(actual.derecho)

    # Inorden: izquierda, raíz, derecha
    def inorden(self, actual):
        if actual is not None:
            self.inorden(actual.izquierdo)
            print(actual.dato, end=" ")
            self.inorden(actual.derecho)

    # Postorden: izquierda, derecha, raíz
    def postorden(self, actual):
        if actual is not None:
            self.postorden(actual.izquierdo)
            self.postorden(actual.derecho)
            print(actual.dato, end=" ")

    # ==========================================
    # MÉTODOS DEL TALLER IMPLEMENTADOS
    # ==========================================

    # Reto 1. contar_nodos()
    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.raiz)

    def _contar_nodos_recursivo(self, actual):
        if actual is None:
            return 0
        return 1 + self._contar_nodos_recursivo(actual.izquierdo) + self._contar_nodos_recursivo(actual.derecho)

    # Reto 2. minimo() y maximo()
    def minimo(self):
        if self.raiz is None:
            return None
        actual = self.raiz
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual.dato

    def maximo(self):
        if self.raiz is None:
            return None
        actual = self.raiz
        while actual.derecho is not None:
            actual = actual.derecho
        return actual.dato

    # Reto 3. altura()
    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, actual):
        if actual is None:
            return 0
        altura_izq = self._altura_recursiva(actual.izquierdo)
        altura_der = self._altura_recursiva(actual.derecho)
        return 1 + max(altura_izq, altura_der)


# ==========================================
# CÓDIGO DE PRUEBA
# ==========================================
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    valores = [10, 5, 15, 3, 7, 12, 18]

    for v in valores:
        arbol.insertar(v)

    print("--- RESULTADOS DE LAS PRUEBAS ---")
    print(f"Total de nodos (esperado 7): {arbol.contar_nodos()}")
    print(f"Mínimo (esperado 3): {arbol.minimo()}")
    print(f"Máximo (esperado 18): {arbol.maximo()}")
    print(f"Altura del árbol (esperado 3): {arbol.altura()}")
    