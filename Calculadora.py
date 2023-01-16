#Calculadora
print("Iniciando calculadora...")

#Variables
acciones = ["0: Menú principal", "1: Suma", "2: Resta", "3: Multiplicación", "4: División", "5: Raíz n", "6: Exponente n", "7: Seno", "8: Salir"]

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
            case 8:
                print("Hasta pronto.")
                isOn = False
        

#Inicio de la aplicación
iniciarCalculadora()