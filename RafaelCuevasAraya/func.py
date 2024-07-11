import time, os, random, csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = []

def limpiar_pantalla():
    os.system("cls")

def menu_principal():
    limpiar_pantalla()
    print("***APLICACIÓN EMPRESA***")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    
def salir():
    limpiar_pantalla()
    print("Finalizando programa...\nDesarrollado por Rafael Cuevas Araya\nRUT 20.525.875-2")
    
def sueldos_aleatorios():
    if len(sueldos) == 0:
        limpiar_pantalla()
        print("Asignando sueldo aleatorio a cada trabajador(a)...")
        time.sleep(2)
        for trabajador in range(len(trabajadores)):
            sueldo = random.randint(300000, 2500000)
            trabajadores[trabajador] = [trabajadores[trabajador], sueldo]
            sueldos.append(sueldo)
        limpiar_pantalla()
        print("Sueldos aleatorios generados exitosamente.\n")
        for trabajador in trabajadores:
            print(trabajador)
        input("Presione una tecla para continuar.")
    else:
        print("ERROR. Ya creaste los sueldos aleatorios correspondientes.")
        time.sleep(3)

def clasificar_sueldos():
    if len(sueldos) > 0:
        limpiar_pantalla()
        print("CLasificando trabajadores(as) según sueldo...")
        time.sleep(2)
        sueldosBajos = []
        sueldosEntre = []
        sueldosSuperiores = []
        
        for trabajador in trabajadores:
            if trabajador[1] < 800000:
                sueldosBajos.append(trabajador)
            elif 800000 <= trabajador[1] <= 2000000:
                sueldosEntre.append(trabajador)
            else:
                sueldosSuperiores.append(trabajador)
        limpiar_pantalla()
        print("Clasificación realizada exitosamente.")
        print(f"\n\t\tSUELDOS MENORES A $800.000.- TOTAL: {len(sueldosBajos)}\n")
        print("\t\tNombre empleado\t\t\tSueldo")
        for bajo in sueldosBajos:
            print(f"\t\t{bajo[0]}\t\t\t${bajo[1]}")
        print(f"\n\t\tSUELDOS ENTRE $800.000.- Y $2.000.000.- TOTAL: {len(sueldosEntre)}\n")
        print("\t\tNombre empleado\t\t\tSueldo")
        for entre in sueldosEntre:
            print(f"\t\t{entre[0]}\t\t\t${entre[1]}")
        print(f"\n\t\tSUELDOS SUPERIORES A $2.000.000.- TOTAL: {len(sueldosSuperiores)}\n")
        print("\t\tNombre empleado\t\t\tSueldo")
        for superior in sueldosSuperiores:
            print(f"\t\t{superior[0]}\t\t\t${superior[1]}")
        print(f"\n\t\tTOTAL SUMA SUELDOS: ${sum(sueldos)}")
        input("Presione una tecla para continuar.")
    else:
        limpiar_pantalla()
        print("ERROR. No existen trabajadores(as) con sueldo asignado, por lo que no es posible realizar la clasificación.")
        time.sleep(3)
        
def sueldo_mayor():
    limpiar_pantalla()
    print("Buscando sueldo más alto...")
    time.sleep(2)
    sueldo_maximo = max(sueldos)
    for trabajador in trabajadores:
        if trabajador[1] == sueldo_maximo:
            print(f"¡Encontrado!\nEl sueldo más alto es ${sueldo_maximo} y corresponde a {trabajador[0]}")
            input("Presione una tecla para continuar.")
    
def sueldo_menor():
    limpiar_pantalla()
    print("Buscando sueldo más bajo...")
    time.sleep(2)
    sueldo_minimo = min(sueldos)
    for trabajador in trabajadores:
        if trabajador[1] == sueldo_minimo:
            print(f"¡Encontrado!\nEl sueldo más bajo es ${sueldo_minimo} y corresponde a {trabajador[0]}")
            input("Presione una tecla para continuar.")
            
def promedio_sueldos():
    limpiar_pantalla()
    print("Calculando promedio...")
    time.sleep(2)
    sueldos = [trabajador[1] for trabajador in trabajadores]
    promedio = round(sum(sueldos) / len(trabajadores))
    print(f"Promedio calculado exitosamente.\nEl promedio de sueldos corresponde a ${promedio}")
    input("Presione una tecla para continuar.")
    
def geometrica_sueldos():
    limpiar_pantalla()
    print("Calculando media geométrica...")
    time.sleep(2)
    sueldos = [trabajador[1] for trabajador in trabajadores]
    multiplica = 1
    for sueldo in sueldos:
        multiplica *= sueldo
    mediaGeometrica = round(multiplica ** (1 / len(sueldos)))
    print(f"Media geométrica calculada exitosamente.\nLa media geométrica de los sueldos corresponde a ${mediaGeometrica}")
    input("Presione una tecla para continuar.")

def ver_estadisticas():
    if len(sueldos) > 0:
        while True:
            limpiar_pantalla()
            print("Ver estadísticas")
            print("1. Sueldo más alto")
            print("2. Sueldo más bajo")
            print("3. Promedio de sueldos")
            print("4. Media geométrica de sueldos")
            print("5. Volver al Menú principal")
            try:
                opc = int(input("Ingrese una opción válida (1-5): "))
                if opc == 1:
                    sueldo_mayor()
                elif opc == 2:
                    sueldo_menor()
                elif opc == 3:
                    promedio_sueldos()
                elif opc == 4:
                    geometrica_sueldos()
                elif opc == 5:
                    print("Volviendo...")
                    time.sleep(1)
                    break
                else:
                    print("ERROR. Opción fuera de rango.")
                    time.sleep(2)
            except:
                print("ERROR. Opción no acepta caracteres.")
                time.sleep(2)
    else:
        limpiar_pantalla()
        print("ERROR. No existen trabajadores(as) con sueldo asignado, por lo que no es posible ver las estadísticas.")
        time.sleep(3)
        
def descargar_archivo():
    limpiar_pantalla()
    print("Descargando archivo...")
    time.sleep(2)
    with open('Reporte_sueldos.csv', mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador in trabajadores:
            writer.writerow(trabajador)
    print("Archivo 'Reporte_sueldos.csv' creado exitosamente.")
    input("Presione una tecla para continuar.")
    
def reporte_sueldos():
    if len(sueldos) > 0:
        limpiar_pantalla()
        print("Creando reporte...")
        time.sleep(2)
        for trabajador in range(len(trabajadores)):
            nombreEmpleado = trabajadores[trabajador][0]
            sueldoBase = trabajadores[trabajador][1]
            dsctoSalud = round(sueldoBase*0.07)
            dsctoAfp = round(sueldoBase*0.12)
            sueldoLiquido = (sueldoBase - dsctoSalud - dsctoSalud)
            trabajadores[trabajador] = [nombreEmpleado, sueldoBase, dsctoSalud, dsctoAfp, sueldoLiquido]
        limpiar_pantalla()
        print("Reporte creado exitosamente.\n\t\t\t***REPORTE DE SUELDOS***")
        print("Nombre empleado\t\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Líquido")
        for trabajador in trabajadores:
            print(f"{trabajador[0]}\t\t${trabajador[1]}\t${trabajador[2]}\t${trabajador[3]}\t${trabajador[4]}")
        descargar = int(input("\n¿Desea descargar el reporte en un archivo formato CSV?\n1. Sí\n2. No\nIngrese una opción válida (1-2): "))
        if descargar == 1:
            descargar_archivo()
        elif descargar == 2:
            input("Entendido. Presione una tecla para continuar.")
        else:
            print("ERROR. Opción no válida. Descarga iniciará automáticamente.")
            time.sleep(2)
            descargar_archivo()
    else:
        limpiar_pantalla()
        print("ERROR. No existen trabajadores(as) con sueldo asignado, por lo que no es posible generar un reporte.")
        time.sleep(3)
