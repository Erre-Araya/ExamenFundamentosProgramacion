from func import *
banderaMenu = True

while banderaMenu:
    menu_principal()
    try:
        opcion = int(input("Ingrese una opción válida (1-5): "))
        if opcion == 1:
            sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir()
            banderaMenu = False
        else:
            print("ERROR. Opción fuera de rango.")
            time.sleep(2)
    except:
        print("ERROR. Opción no acepta caracteres.")
        time.sleep(2)