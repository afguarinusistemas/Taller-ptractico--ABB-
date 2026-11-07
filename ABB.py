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

    # izquierda, raíz, derecha
    def inorden(self, actual):
        if actual is not None:
            self.inorden(actual.izquierdo)
            print(actual.dato, end=" ")
            self.inorden(actual.derecho)

    # izquierda, derecha, raíz
    def postorden(self, actual):
        if actual is not None:
            self.postorden(actual.izquierdo)
            self.postorden(actual.derecho)
            print(actual.dato, end=" ")


arbol = ArbolBinarioBusqueda()


for valor in [10, 5, 15, 3, 7, 12, 18]:
    arbol.insertar(valor)

print(arbol.buscar(7))  # True
print(arbol.buscar(20))  # False

print("Preorden:")
arbol.preorden(arbol.raiz)  # Salida: 10 5 3 7 15 12 18

print("\nInorden:")
arbol.inorden(arbol.raiz)  # Salida: 3 5 7 10 12 15 18

print("\nPostorden:")
arbol.postorden(arbol.raiz)  # Salida: 3 7 5 12 18 15 10


