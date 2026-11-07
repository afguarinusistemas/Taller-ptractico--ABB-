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
            return True
        else:
            return self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, actual, dato):
        if dato == actual.dato:
            return False  # Rechaza duplicados

        if dato < actual.dato:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(dato)
                return True
            else:
                return self._insertar_recursivo(actual.izquierdo, dato)
        else:
            if actual.derecho is None:
                actual.derecho = Nodo(dato)
                return True
            else:
                return self._insertar_recursivo(actual.derecho, dato)

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

    # Impresión directa mediante Inorden (sin usar listas ni arreglos de Python)
    def inorden(self, actual):
        if actual is not None:
            self.inorden(actual.izquierdo)
            print(actual.dato, end=" ")
            self.inorden(actual.derecho)

    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.raiz)

    def _contar_nodos_recursivo(self, actual):
        if actual is None:
            return 0
        return 1 + self._contar_nodos_recursivo(actual.izquierdo) + self._contar_nodos_recursivo(actual.derecho)

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


def leer_entero(mensaje):
    """Función auxiliar para validar que el usuario ingrese únicamente números enteros."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("[ERROR] Entrada inválida. Debe ingresar un número entero (ej. 104).")


def main():
    arbol = ArbolBinarioBusqueda()

    while True:
        print("\n" + "=" * 45)
        print("   SISTEMA DE CÓDIGOS DE ESTUDIANTES (ABB)")
        print("=" * 45)
        print("1. Registrar un código de estudiante")
        print("2. Buscar un código")
        print("3. Mostrar todos los códigos ordenados (Inorden)")
        print("4. Consultar cantidad total de códigos")
        print("5. Consultar código menor y mayor")
        print("6. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            codigo = leer_entero("Ingrese el código del estudiante a registrar: ")
            if arbol.insertar(codigo):
                print(f"[ÉXITO] El código {codigo} fue registrado correctamente.")
            else:
                print(f"[ADVERTENCIA] El código {codigo} ya existe. No se admiten duplicados.")

        elif opcion == "2":
            if arbol.raiz is None:
                print("[INFO] El árbol está vacío.")
            else:
                codigo = leer_entero("Ingrese el código a buscar: ")
                if arbol.buscar(codigo):
                    print(f"[RESULTADO] El código {codigo} SÍ se encuentra registrado (True).")
                else:
                    print(f"[RESULTADO] El código {codigo} NO se encuentra en el sistema (False).")

        elif opcion == "3":
            if arbol.raiz is None:
                print("[INFO] El árbol está vacío.")
            else:
                print("\nCódigos ordenados de menor a mayor:")
                print("[ ", end="")
                arbol.inorden(arbol.raiz)
                print("]")

        elif opcion == "4":
            total = arbol.contar_nodos()
            print(f"[INFO] Cantidad total de códigos registrados: {total}")

        elif opcion == "5":
            min_val = arbol.minimo()
            max_val = arbol.maximo()
            if min_val is None:
                print("[INFO] El árbol está vacío.")
            else:
                print(f"[INFO] Código MENOR: {min_val}")
                print(f"[INFO] Código MAYOR: {max_val}")

        elif opcion == "6":
            print("\n¡Gracias por utilizar el sistema! Saliendo...")
            break
        else:
            print("[ERROR] Opción no válida. Por favor seleccione un número entre 1 y 6.")


if __name__ == "__main__":
    main()


    