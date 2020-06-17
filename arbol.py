class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
 
def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)

def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato)

def buscar_dato(raiz, dato):
    if raiz is None:
        return False
    elif raiz.dato == dato:
        return True
    elif dato < raiz.dato:
        return buscar_dato(raiz.izquierda, dato)
    else:
        return buscar_dato(raiz.derecha, dato)


def main():
    numeros = []
    cant = int(input('Introduzca la cantidad de numeros que desea agregar al arbol binario: '))
    
    for i in range(cant):
        num = int(input('Introduzca el numero: '))
        numeros.append(num)

    raiz = Nodo(numeros[0])
    
    for i in numeros:
        if i != numeros[0] :
            print(i)
            insertar(raiz, Nodo(i))

    print('Inorden')
    inorden(raiz)



main()
