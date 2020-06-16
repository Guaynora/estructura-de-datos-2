class Node:
    anterior = None
    siguiente = None
    def __init__(self, nombre, habilidad, anterior, siguiente):
        self.nombre = nombre
        self.habilidad = habilidad
        self.anterior = anterior
        self.siguiente = siguiente

    def getNombre(self):
        return self.nombre

    def getHabilidad(self):
        return self.habilidad

    def getAnterior(self):
        return self.anterior

    def getSiguiente(self):
        return self.siguiente

class Lista:
    def agregarInicio(self, nombre, habilidad):
        if(self.validar()):
            nuevo = Nodo(nombre, habilidad, None, None)
            self.inicio = nuevo
            self.fin = nuevo
        else:
            nuevo = Nodo(nombre,habilidad, None, self.inicio)
            self.inicio.anterior = nuevo
            self.inicio = nuevo

    def agregar(self):
        nombre = input("Digite nombre: ")
        precio = float(input("Digite precio: "))
        cantidad = int(input("Digite cantidad: "))

        temp = self.inicio
        while temp != None:
            if temp.codigo == codigo:
                print ("Error, ya existe un producto con el codigo " + codigo)
                return
            elif temp.nombre == nombre:
                print ("Error, ya existe un producto con el nombre " + nombre)
                return
            temp = temp.siguiente

        self.agregarInicio(nombre, habilidad)

class Movimiento:
    def intercambiar(self):

    def mirar(self):
    
    def anunciar(self):
        

class Game:
    print("Cantidad de jugadores\n")
    print("1. 4 jugadores\n")
    print("2. 5 jugadores\n")
    opj = int(input())


class Main:
    while True:
        print("-----MASCARADE-----\n")
        print("1. Empezar a jugar\n")
        print("2. Reglas\n")
        opc = int(input())
        if opc = 1:
