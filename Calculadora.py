#Calculadora

import numpy as np

print("Iniciando calculadora...")

#Variables
acciones = ["0: Menú principal", "1: Suma", "2: Resta", "3: Multiplicación", "4: División", "5: Raíz n", "6: Exponente n", "7: Seno", "8: Salir"]

def suma():
    sumando1 = float(input("Ingresa el primer sumando: "))
    sumando2 = float(input("Ingresa el segundo sumando: "))
    print("La suma es igual a ", np.add(sumando1,sumando2))

def resta():
    minuendo = float(input("Ingresa el minuendo: "))
    sustraendo = float(input("Ingresa el sustraendo: "))
    print("La resta es igual a ", np.subtract(minuendo,sustraendo))

def multiplicacion():
    factor1 = float(input("Ingresa el primer valor: "))
    factor2 = float(input("Ingresa el segundo valor: "))
    print("El resultado es ", np.multiply(factor1,factor2))

def division():
    dividendo = float(input("Ingresa el dividendo: "))
    divisor = float(input("Ingresa el divisor: "))
    print("El resultado es ", np.divide(dividendo,divisor))

def raiz():
    base = int(input("Ingresa la base: "))
    raiz = int(input("Ingresa la raiz: "))
    print("El resultado de la raíz es :", base**(1/raiz))

def exponente():
    base = int(input("Ingresa la base: "))
    potencia = int(input("Ingresa la potencia: "))
    print("El resultado del exponente es :", base**potencia)

def seno():
    grados = int(input("Ingresa los grados: "))
    radianes = grados*np.pi/180
    print("El seno de ", grados, "° es ", np.sin(radianes))

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
            case 2:
                print("Resta:")
                resta()
                repetir(resta)
            case 3:
                print("Multiplicación:")
                multiplicacion()
                repetir(multiplicacion)
            case 4:
                print("División:")
                division()
                repetir(division)
            case 5:
                print("Raíz:")
                raiz()
                repetir(raiz)
            case 6:
                print("Exponente:")
                exponente()
                repetir(exponente)
            case 7:
                print("Seno:")
                seno()
                repetir(seno)
            case 8:
                print("Hasta pronto...")
                isOn = False
        

#Inicio de la aplicación
iniciarCalculadora()