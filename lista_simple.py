import os
#prograama de ista simple para python3
#shai jesus gallegos espinosa 21/oct/2019
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

class nodo:
    def __init__(self,val):
        self.valor=val
        self.next=None

    def get_valor(self):
        return self.valor

class Lista:
    def __init__(self):
        self.top=None

    def anadir_al_final(self, elemento):
        if not self.top:
            self.top =nodo(elemento)
            return
        puntero=self.top
        while puntero.next:
            puntero=puntero.next
        puntero.next=nodo(elemento)

    def  anadir_al_inicio(self,elemento):
        if not self.top:
            self.top =nodo(elemento)
            return
        puntero=self.top
        self.top=nodo(elemento)
        self.top.next=puntero

    def  imprimir_lista(self):
        puntero=self.top
        while puntero:
            print(puntero.get_valor())
            puntero=puntero.next

    def borrar_al_inicio(self):
        if self.top:
            self.top=self.top.next

    def borrar_al_final(self):
        if self.top:
            puntero = self.top
            while puntero.next.next:
                puntero = puntero.next
            puntero.next = None

    def longitud(self):
        longitud=0
        if self.top:
            puntero = self.top
            while puntero:
                longitud += 1
                puntero = puntero.next
        print(longitud)

def menu():
    variable_menu=True
    lista=Lista()
    while variable_menu==True:
        limpiar_pantalla()
        print("Programa de lista simple ")
        print("a) Agregar al inicio")
        print("b) Agregar al final")
        print("c) Borrar al inicio")
        print("d) Borrar al final ")
        print("e) Obtener longitud ")
        print("f) imprimir lista")
        print("g) salir")
        option=input("selecciona una opcion: ")
        if option=="a":
            dato=int(input("Ingrese un numero: "))
            lista.anadir_al_inicio(dato)
            continue

        elif option=="b":
            dato=int(input("Ingrese un numero: "))
            lista.anadir_al_final(dato)
            continue

        elif option == "c":
            lista.borrar_al_inicio()
            continue

        elif option == "d":
            lista.borrar_al_final()
            continue

        elif option == "e":
            lista.longitud()
            continue

        elif option == "f":
            lista.imprimir_lista()
            input("presione una tecla para continuar....")
            continue

        elif option == "g":
            break

        else:
            continue

menu()