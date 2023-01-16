#Calculadora

import numpy as np

print("Iniciando calculadora...")

#Variables
acciones = ["0: Menú principal", "1: Suma", "2: Resta", "3: Multiplicación", "4: División", "5: Raíz n", "6: Exponente n", "7: Seno", "8: Salir"]

def suma():
    sumando1 = int(input("Ingresa el primer sumando: "))
    sumando2 = int(input("Ingresa el segundo sumando: "))
    print("La suma es igual a ", np.add(sumando1,sumando2))

def repetir(func):
    repetir = int(input("""¿Qué deseas hacer?
    0: Volver al menú principal
    1: Repetir operación
    """))
    while repetir != 0:
        func()
        repetir = int(input("""¿Qué deseas hacer?
        0: Volver al menú principal
        1: Repetir operación
        """))
    

def iniciarCalculadora():
    isOn = True
    while isOn:
        print("Seleccione la opción deseada:")
        for x in acciones:
            print(x)
        accion = int(input())
        match accion:
            case 0:
                print("Menú principal")
            case 1:
                print("Suma:")
                suma()
                repetir(suma)
            case 8:
                print("Hasta pronto...")
                isOn = False
        

#Inicio de la aplicación
iniciarCalculadora()