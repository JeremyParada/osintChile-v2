import argparse
import sources.nombrerutyfirma as nrf
import sources.salud as salud
import sources.soap as soap
import sources.sii as sii
import sources.volanteomaleta as volanteomaleta
import sources.numverify as numverify
import sources.masterchileapkBday as mchaBday
import sources.celuzador as celuzador


def main():
    while True:
        print("Seleccione una opción:")
        print("1. Buscar por RUT")
        print("2. Buscar por Patente")
        print("3. Buscar por Teléfono")
        print("4. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == '1':
            rut = input("Ingrese el RUT de la persona a buscar (formato: 11111111-1): ")
            salud.busqueda(rut=rut)
            nrf.busqueda(rut=rut)
            sii.busqueda(rut=rut)
            volanteomaleta.busqueda(rut=rut)
            mchaBday.busqueda(rut=rut)
        elif opcion == '2':
            patente = input("Ingrese la patente del vehículo a buscar (formato: aabb11): ")
            print('---En Construccion, se aceptan contribuciones---')
            soap.busqueda(patente=patente)
            volanteomaleta.busqueda(patente=patente)
        elif opcion == '3':
            telefono = input("Ingrese el teléfono a buscar (formato: 56999999999): ")
            print('---En Construccion, se aceptan contribuciones---')
            numverify.busqueda(telefono=telefono)
            celuzador.busqueda(telefono=telefono)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
