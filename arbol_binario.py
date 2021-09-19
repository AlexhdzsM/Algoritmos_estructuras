#Nodo
class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None

#Agregar datos

def __agregar_recursivo(self, nodo, dato):
    if dato < nodo.dato:
        if nodo.izquierda is None:
            nodo.izquierda = Nodo(dato)
        else:
            self.__agregar_recursivo(nodo.izquierda, dato)
    else:
        if nodo.derecha is None:
            nodo.derecha = Nodo(dato)
        else:
            self.__agregar_recursivo(nodo.derecha, dato)


#Recorridos

def __inorden_recursivo(self, nodo):
    if nodo is not None:
        self.__inorden_recursivo(nodo.izquierda)
        print(nodo.dato, end=", ")
        self.__inorden_recursivo(nodo.derecha)

def __preorden_recursivo(self, nodo):
    if nodo is not None:
        print(nodo.dato, end=", ")
        self.__preorden_recursivo(nodo.izquierda)
        self.__preorden_recursivo(nodo.derecha)

def __postorden_recursivo(self, nodo):
    if nodo is not None:
        self.__postorden_recursivo(nodo.izquierda)
        self.__postorden_recursivo(nodo.derecha)
        print(nodo.dato, end=", ")

#Busquda de datos

def __buscar(self, nodo, busqueda):
    if nodo is None:
        return None
    if nodo.dato == busqueda:
        return nodo
    if busqueda < nodo.dato:
        return self.__buscar(nodo.izquierda, busqueda)
    else:
        return self.__buscar(nodo.derecha, busqueda)


#Arbol
class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)


#Implementacion del arbol
arbol_numeros = Arbol(5)
arbol_numeros.agregar(1984)
arbol_numeros.agregar(60)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(10)
arbol_numeros.agregar(25)
arbol_numeros.agregar(59)
arbol_numeros.agregar(64)
arbol_numeros.agregar(10)
arbol_numeros.agregar(19)
arbol_numeros.agregar(23)
arbol_numeros.agregar(18)
arbol_numeros.agregar(1)
arbol_numeros.agregar(2013)
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()

busqueda = int(input("Ingresa un número para buscar en el árbol: "))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")

new = int(input("Agregar numero al arbol: "))
arbol_numeros.agregar(new)
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()

